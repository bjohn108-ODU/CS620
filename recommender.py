import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans

def getDifferences(responses, centroids):
  differences = []
  for i in range(len(centroids)):
      leftCentroid = centroids[i][0]
      rightCentroid = centroids[i][1]
      if leftCentroid[0] > rightCentroid[0]:
         temp = leftCentroid
         leftCentroid = rightCentroid
         rightCentroid = temp
      diff = rightCentroid[1] - leftCentroid[1]
      if responses[i] == "No":
         diff = diff * -1
      if i < 2:
         diff = diff * -1
      differences.append(diff)
  return differences

def getBehavior(differences, responses):
    diff = differences
    res = responses
    if res[2] == "Yes":
      res[2] = "No"
    else:
      res[2] = "Yes"
    
    if res[3] == "Yes":
      res[3] = "No"
    else:
      res[3] = "Yes"
    max = 0
    loc = -1
    for i in range(len(diff)):
      if diff[i] > max and res[i] == "No":
        max = diff[i]
        loc = i

    match loc:
       case 0:
          return "You should try eating at least one vegetable per day."
       case 1:
          return "You should try eating at least one fruit per day."
       case 2:
          return "You should try to cut back on soda consumption, or cut it out entirely."
       case 3:
          return "You should try spending less time watching TV."
       case 4:
          return "You should try engaging in at least one hour of physical activity every day."
       case 5:
          return "You should try receiving physical education on a daily basis."
       case _:
          return "You should try eating more vegetables per day."

def recommend(location, stratifications, responses, df):

  topics = ["VegetableValue", "FruitValue", "SodaValue", "TvValue", "PhysicalActivityValue", "PhysicalEducationValue"]
  if location != "Prefer not to say":
    subset = df[df["LocationDesc"] == location]
  else:
    subset = df

  obeseCentroids = []
  overweightCentroids = []
  hasStrat = False
  #What if instead, I created different subDataFrames for each stratification, combined them into one, and go through the calculations on just that?
  working = pd.DataFrame()
  for i in stratifications:
    if i == "Prefer not to say":
      continue
    if hasStrat == False:
      hasStrat = True
      working = subset[subset["Stratification1"] == i]
    else:
      current = subset[subset["Stratification1"] == i]
      working.merge(current)
  #If the user selected "Prefer not to say" on all Stratifications, use the total values instead
  if ((hasStrat == False)):
    working = subset[subset["Stratification1"] == "Total"]
  
  #If there are not enough rows based on the filtering, use data from all locations that match stratifications
  elif len(working) < 10:
    working = pd.DataFrame()
    hasStrat = False
    for i in stratifications:
      if i == "Prefer not to say":
        continue
      if hasStrat == False:
        hasStrat = True
        working = df[df["Stratification1"] == i]
      else:
        current = df[df["Stratification1"] == i]
        working.merge(current)

  #If there is still not enough data, use the total values from all locations to provide a generic feedback
  if len(working) < 10:
    working = df[df["Stratification1"] == "Total"]

  #Run KMeans Clustering for All six behaviors against both obese and overweight values. Add the centroids to their respective arrays
  for j in range(6):
      kmeans = KMeans(n_clusters=2)
      current = working[[topics[j], "ObeseValue"]]
      kmeans.fit(current)
      labels = kmeans.labels_
      #Get the centroids
      centroids = kmeans.cluster_centers_
      #Add centroid locations to array
      obeseCentroids.append(centroids)

      kmeans = KMeans(n_clusters=2)
      current = working[[topics[j], "OverweightValue"]]
      kmeans.fit(current)
      labels = kmeans.labels_
      centroids = kmeans.cluster_centers_
      overweightCentroids.append(centroids)
  obeseDifferences = getDifferences(responses, obeseCentroids)
  overweightDifferences = getDifferences(responses, overweightCentroids)
  obeseBehavior = getBehavior(obeseDifferences, responses)
  overweightBehavior = getBehavior(overweightDifferences, responses)

  return [obeseBehavior, overweightBehavior]

def test():
    location = "Virginia"
    strat = ["Non-Hispanic White", "Male", "12th"]
    responses = ["Yes", "No", "Yes", "No", "Yes", "No"]
    df = pd.read_csv("CleanData.csv")
    print(recommend(location, strat, responses, df))

    

if __name__ == "__main__":
    test()