import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
#print(visits.head())
#print(cart.head())
#print(checkout.head())
#print(purchase.head())

visits_cart=pd.merge(visits,cart,how='left')
print(len(visits_cart))
null_cart=visits_cart['cart_time'].isnull().sum()
print(null_cart)

no_cart=float(null_cart)/len(visits_cart)
print(no_cart) # % of visits without placing item in cart

cart_checkout=pd.merge(cart,checkout,how='left')
#print(cart_checkout.head())

null_checkout=cart_checkout['checkout_time'].isnull().sum()
#print(null_checkout)
no_checkout=float(null_checkout)/len(cart_checkout)
#print(no_checkout)

all_data=visits.merge(cart,how='left').merge(checkout,how='left').merge(purchase,how='left')
print(all_data.head())

checkout_1=len(all_data[all_data['checkout_time'].notnull()])
purchase_time_0=len(all_data[all_data['purchase_time'].isnull()])
check1purchase0=float(purchase_time_0)/checkout_1
#print(check1purchase0)

all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time

print(all_data.time_to_purchase)
print(all_data.time_to_purchase.mean())
