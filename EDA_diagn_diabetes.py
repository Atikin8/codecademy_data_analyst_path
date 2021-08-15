import codecademylib3
import pandas as pd
import numpy as np

# code goes here
diabetes_data=pd.read_csv("diabetes.csv")
print(diabetes_data.head())

diabetes_data.info() #9 columns. 768 rows
print(diabetes_data.shape)
#print(diabetes_data.isnull().sum())

print(diabetes_data.describe())
#glucose, bloodpressure, skinthickness, insulin, bmi have minimum values of 0; These values also seem to be way off from their respective medians and means, another indicator that something is off.
#One way to interpret this is that these are missing values in the data.

diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.NaN)

print(diabetes_data.isnull().sum())
#Print out all of the rows that contain missing (null) values
print(diabetes_data[diabetes_data.isnull().any(axis=1)])

print(diabetes_data.dtypes)

print(diabetes_data['Outcome'].unique())
#replace "O" with 0 and change to integer
diabetes_data['Outcome']=diabetes_data['Outcome'].replace("O","0").astype('int')
print(diabetes_data.dtypes)
