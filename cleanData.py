#Import the raw data and store it
#The originalData dataframe is meant to be READ ONLY in case I need to reference the unedited data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate
originalData = pd.read_csv("https://raw.githubusercontent.com/bjohn108-ODU/CS620/refs/heads/main/HealthData.csv")

#We will be working with df
df = originalData.copy()
print(df.info())
print(tabulate(df.head(10), headers = 'keys', tablefmt = 'psql'))
print("Datasource")
df.groupby('Datasource').count()
df.drop("Datasource", axis=1, inplace=True)
print(tabulate(df.head(10), headers = 'keys', tablefmt = 'psql'))
df.groupby('Topic').count()
print("Before\n", df.describe())
df.drop(df[(df.Data_Value_Footnote=="Data not available because sample size is insufficient or data not reported.")].index, inplace=True)
print("After\n", df.describe())
df.drop(["Data_Value_Footnote", "Data_Value_Footnote_Symbol"], axis=1, inplace=True)
print(tabulate(df.head(10), headers = 'keys', tablefmt = 'psql'))
df.groupby('DataValueTypeID').count()
df.drop("DataValueTypeID", axis=1, inplace=True)
print(tabulate(df.head(10), headers = 'keys', tablefmt = 'psql'))
df.groupby('StratificationCategoryId1').count()
print(df.loc[df['Data_Value'] != df["Data_Value_Alt"]])
df.drop("Data_Value_Alt", axis=1, inplace=True)
print(tabulate(df.head(10), headers = 'keys', tablefmt = 'psql'))
df.groupby('Class').count()
df.groupby('Topic').count()
print(df.loc[df['Class'] != df["Topic"]])
df_ct = df[(df['Topic'] == 'Physical Activity - Behavior') & (df['Class'] != 'Physical Activity')]
print(tabulate(df_ct.head(10), headers = 'keys', tablefmt = 'psql'))
df_ct = df[(df['Topic'] == 'Sugar Drinks - Behavior') & (df['Class'] != 'Sugar Drinks')]
print(tabulate(df_ct.head(10), headers = 'keys', tablefmt = 'psql'))
df_ct = df[(df['Topic'] == 'Fruits and Vegetables - Behavior') & (df['Class'] != 'Fruits and Vegetables')]
print(tabulate(df_ct.head(10), headers = 'keys', tablefmt = 'psql'))
df_ct = df[(df['Topic'] == 'Television Viewing - Behavior') & (df['Class'] != 'Television Viewing')]
print(tabulate(df_ct.head(10), headers = 'keys', tablefmt = 'psql'))
df.drop('Topic', axis=1, inplace=True)
print(tabulate(df.head(10), headers = 'keys', tablefmt = 'psql'))
df.groupby('Data_Value_Unit').count()
df.drop('Data_Value_Unit', axis=1, inplace=True)
print(tabulate(df.head(10), headers = 'keys', tablefmt = 'psql'))
df.groupby('Data_Value_Type').count()
df.drop('Data_Value_Type', axis=1, inplace=True)
print(tabulate(df.head(10), headers = 'keys', tablefmt = 'psql'))
df.groupby('LocationDesc').count()
df.groupby('LocationAbbr').count()
df.groupby('StratificationCategory1').count()
df.groupby('Question').count()
df.groupby("QuestionID").count()
print(tabulate(df.head(10), headers = 'keys', tablefmt = 'psql'))
df2 = pd.DataFrame()
df2["YearStart"] = df["YearStart"]
df2["YearEnd"] = df["YearEnd"]
df2["LocationAbbr"] = df["LocationAbbr"]
df2["LocationDesc"] = df["LocationDesc"]
df2["StratificationCategory1"] = df["StratificationCategory1"]
df2["Stratification1"] = df["Stratification1"]
df2["StratificationCategoryID1"] = df["StratificationCategoryId1"]
df2["StratificationID1"] = df["StratificationID1"]
df2["LocationID"] = df["LocationID"]
df2 = df2.drop_duplicates()
df2["OverweightValue"] = np.nan
df2["ObeseValue"] = np.nan
df2["TvValue"] = np.nan
df2["SodaValue"] = np.nan
df2["VegetableValue"] = np.nan
df2["FruitValue"] = np.nan
df2["PhysicalActivityValue"] = np.nan
df2["PhysicalEducationValue"] = np.nan
print(tabulate(df2.head(10), headers = 'keys', tablefmt = 'psql'))
obesity = df.loc[df["QuestionID"] == "Q038"]
overweight = df.loc[df["QuestionID"] == "Q039"]
soda = df.loc[df["QuestionID"] == "Q058"]
tv = df.loc[df["QuestionID"] == "Q059"]
fruit = df.loc[df["QuestionID"] == "Q020"]
vegetable = df.loc[df["QuestionID"] == "Q021"]
physicalActivity = df.loc[df["QuestionID"] == "Q048"]
physicalEducation = df.loc[df["QuestionID"] == "Q049"]

merged_df = df2.merge(obesity[['YearStart', 'YearEnd', 'Stratification1', 'LocationAbbr', 'Data_Value']],
                      on=['YearStart', 'YearEnd', 'Stratification1', 'LocationAbbr'],
                      how='left')

df2['ObeseValue'] = merged_df['Data_Value']

merged_df = df2.merge(overweight[['YearStart', 'YearEnd', 'Stratification1', 'LocationAbbr', 'Data_Value']],
                      on=['YearStart', 'YearEnd', 'Stratification1', 'LocationAbbr'],
                      how='left')

df2['OverweightValue'] = merged_df['Data_Value']

merged_df = df2.merge(soda[['YearStart', 'YearEnd', 'Stratification1', 'LocationAbbr', 'Data_Value']],
                      on=['YearStart', 'YearEnd', 'Stratification1', 'LocationAbbr'],
                      how='left')

df2['SodaValue'] = merged_df['Data_Value']

merged_df = df2.merge(tv[['YearStart', 'YearEnd', 'Stratification1', 'LocationAbbr', 'Data_Value']],
                      on=['YearStart', 'YearEnd', 'Stratification1', 'LocationAbbr'],
                      how='left')

df2['TvValue'] = merged_df['Data_Value']

merged_df = df2.merge(fruit[['YearStart', 'YearEnd', 'Stratification1', 'LocationAbbr', 'Data_Value']],
                      on=['YearStart', 'YearEnd', 'Stratification1', 'LocationAbbr'],
                      how='left')

df2['FruitValue'] = merged_df['Data_Value']

merged_df = df2.merge(vegetable[['YearStart', 'YearEnd', 'Stratification1', 'LocationAbbr', 'Data_Value']],
                      on=['YearStart', 'YearEnd', 'Stratification1', 'LocationAbbr'],
                      how='left')

df2['VegetableValue'] = merged_df['Data_Value']

merged_df = df2.merge(physicalActivity[['YearStart', 'YearEnd', 'Stratification1', 'LocationAbbr', 'Data_Value']],
                      on=['YearStart', 'YearEnd', 'Stratification1', 'LocationAbbr'],
                      how='left')

df2['PhysicalActivityValue'] = merged_df['Data_Value']

merged_df = df2.merge(physicalEducation[['YearStart', 'YearEnd', 'Stratification1', 'LocationAbbr', 'Data_Value']],
                      on=['YearStart', 'YearEnd', 'Stratification1', 'LocationAbbr'],
                      how='left')

df2['PhysicalEducationValue'] = merged_df['Data_Value']

print(tabulate(df2.head(10), headers = 'keys', tablefmt = 'psql'))
df2.describe()
df2 = df2.dropna()
print(tabulate(df2.head(10), headers = 'keys', tablefmt = 'psql'))

df2.to_csv("CleanData.csv")