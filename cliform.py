import pandas as pd
import threading
import recommender

df = pd.DataFrame()
def getData():
    global df
    df = pd.read_csv("https://raw.githubusercontent.com/bjohn108-ODU/CS620/refs/heads/main/CleanData.csv")

reader = threading.Thread(target=getData)
reader.start()

stratifications = []
responses = []

location_options= [ "Prefer not to say",
                    "Alabama",
                    "Alaska",
                    "Arizona",
                    "Arkansas",
                    "California",
                    "Colorado",
                    "Connecticut",
                    "Delaware",
                    "District of Columbia",
                    "Florida",
                    "Georgia",
                    "Guam",
                    "Hawaii",
                    "Idaho",
                    "Illinois",
                    "Indiana",
                    "Iowa",
                    "Kansas",
                    "Kentucky",
                    "Louisiana",
                    "Maine",
                    "Maryland",
                    "Massachusetts",
                    "Michigan",
                    "Mississippi",
                    "Missouri",
                    "Montana",
                    "National",
                    "Nebraska",
                    "Nevada",
                    "New Hampshire",
                    "New Jersey",
                    "New Mexico",
                    "New York",
                    "North Carolina",
                    "North Dakota",
                    "Ohio",
                    "Oklahoma",
                    "Pennsylvania",
                    "Puerto Rico",
                    "Rhode Island",
                    "South Carolina",
                    "South Dakota",
                    "Tennessee",
                    "Texas",
                    "Utah",
                    "Vermont",
                    "Virgin Islands",
                    "Virginia",
                    "West Virginia",
                    "Wisconsin",
                    "Wyoming"
                ]

race_options=[
    "Prefer not to say"  
    "American Indian/Alaska Native",
    "Asian",
    "Hawaiian/Pacific Islander",
    "Hispanic",
    "Non-Hispanic Black",
    "Non-Hispanic White"
]

gender_options = [
    "Prefer not to say",
    "Male",
    "Female"
]

grade_options = [
    "Prefer not to say",
    "9th",
    "10th",
    "11th",
    "12th"
]

question_options = [
    "Yes",
    "No"
]

questions = [
    "Do you eat at least one vegetable per day on average?",
    "Do you eat at least one fruit per day on average?",
    "Do you drink at least one soda per day on average?",
    "Do you watch TV for at least three hours per day on average?",
    "Do you engage in at least one hour of moderate to intense physical activity per day on average?",
    "Do you participate in at least one hour of Physical Education per day on average?"
]


print("Select a location (Enter the number):\n")
for i in range(len(location_options)):
    print(i, location_options[i])
location = input("Enter the number of your location:")
location = location_options[int(location)]

print("What is your race?")
for i in range(len(race_options)):
    print(i, race_options[i])
race = input("Enter the number:")
stratifications.append(race_options[int(race)])

print("What is your gender?")
for i in range(len(gender_options)):
    print(i, gender_options[i])
gender = input("Enter the number:")
stratifications.append(gender_options[int(gender)])

print("What is your grade level?")
for i in range(len(grade_options)):
    print(i, grade_options[i])
grade = input("Enter the number:")
stratifications.append(grade_options[int(grade)])

for i in range(6):
    print(questions[i])
    for j in range(len(question_options)):
        print(j, question_options[j])
    num = input("Enter the number:")
    if int(num) == 0:
        responses.append("Yes")
    else:
        responses.append("No")

recommendation = recommender.recommend(location, stratifications, responses, df)

if(recommendation[0] == recommendation[1]):
    print("To best reduce your risk of obesity and overweight status, ", recommendation[0])
else:
    print("To best reduce your risk of obesity, ", recommendation[0], "\nTo best reduce your risk of overweight status, ", recommendation[1])