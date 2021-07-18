import pandas as pd
import numpy as np

car_eval = pd.read_csv('car_eval_dataset.csv')
print(car_eval.head())

print(car_eval['manufacturer_country'].value_counts())
fourth=car_eval['manufacturer_country'].value_counts().index[3]
print(fourth)

print(car_eval['manufacturer_country'].value_counts(normalize=True))

print(car_eval['buying_cost'].unique())
buying_cost_categories=['low','med','high','vhigh']
car_eval['buying_cost']=pd.Categorical(car_eval['buying_cost'],buying_cost_categories,ordered=True)
c=np.median(car_eval['buying_cost'].cat.codes)
print(buying_cost_categories[int(c)])

print(car_eval['luggage'].value_counts(normalize=True,dropna=False))
print(car_eval['luggage'].value_counts()/len(car_eval['luggage']))

print((car_eval['doors']=='5more').sum())
print((car_eval['doors']=='5more').mean())
