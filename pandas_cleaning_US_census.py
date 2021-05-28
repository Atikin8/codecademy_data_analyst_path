import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob

files=glob.glob('states*.csv')

dfs=[]

for file in files:
  data=pd.read_csv(file)
  dfs.append(data)

us_census=pd.concat(dfs)

#print(us_census.head())
#print(us_census.dtypes)

us_census['Income']=us_census['Income'].replace('[\$,]','',regex=True)
us_census['Income']=pd.to_numeric(us_census["Income"])

us_census['Men']=us_census['GenderPop'].str.split('M_',expand=True)[0]
us_census['Men']=pd.to_numeric(us_census['Men'])

us_census['Women']=us_census['GenderPop'].str.split('M_',expand=True)[1]
us_census['Women']=us_census['Women'].replace('[F]','',regex=True)
us_census['Women']=pd.to_numeric(us_census['Women'])

print(us_census.head())
#print(us_census.dtypes)

us_census['Women']=us_census['Women'].fillna(us_census['TotalPop']-us_census['Men'])
us_census=us_census.drop_duplicates()

print(us_census.head())
plt.scatter(us_census['Women'], us_census['Men']) 
plt.show()
plt.close()

us_census['Hispanic']=pd.to_numeric(us_census["Hispanic"].replace('[\%]','',regex=True))
us_census['White']=pd.to_numeric(us_census["White"].replace('[\%]','',regex=True))
us_census['Black']=pd.to_numeric(us_census["Black"].replace('[\%]','',regex=True))
us_census['Native']=pd.to_numeric(us_census["Native"].replace('[\%]','',regex=True))
us_census['Asian']=pd.to_numeric(us_census["Asian"].replace('[\%]','',regex=True))
us_census['Pacific']=pd.to_numeric(us_census["Pacific"].replace('[\%]','',regex=True))
us_census=us_census.round(2)
print(us_census.head())

plt.hist(us_census['Black']) 
plt.show()
plt.close() 








