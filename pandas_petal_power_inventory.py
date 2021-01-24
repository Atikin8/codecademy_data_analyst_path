import codecademylib
import pandas as pd

inventory=pd.read_csv('inventory.csv')

print(inventory.head(10))

staten_island=inventory[inventory['location']=='Staten Island']

product_request=staten_island['product_description']

seed_request=inventory[(inventory['location']=='Brooklyn') & (inventory['product_type']=='seeds')]

print(seed_request)

inventory['in_stock']=inventory.apply(lambda row: True if row['quantity']>0 else False, axis=1)

inventory['total_value']=inventory['price']*inventory['quantity']

combine_lambda=lambda row: '{} - {}'.format(row['product_type'],row['product_description'])

inventory['full_description']=inventory.apply(combine_lambda,axis=1)

print(inventory)
