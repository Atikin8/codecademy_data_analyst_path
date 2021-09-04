import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels
import matplotlib.pyplot as plt
import math
import codecademylib3


## Read in Data
flight = pd.read_csv("flight.csv")
print(flight.head())

## Task 1
print(np.min(flight['coach_price']))
print(np.max(flight['coach_price']))
print(np.mean(flight['coach_price']))
sns.histplot(flight['coach_price'])
plt.show()
plt.clf()

## Task 2
hours_8=flight[flight['hours']==8]
#print(hours_8)
print(np.min(hours_8['coach_price']))
print(np.max(hours_8['coach_price']))
print(np.mean(hours_8['coach_price']))
sns.histplot(hours_8['coach_price'])
plt.show()
plt.clf()

## Task 3
sns.histplot(flight['delay'][flight['delay']<400])
plt.show()
plt.clf()
#10 min delays are common
## Task 4

perc = 0.1
flight_sub = flight.sample(n = int(flight.shape[0]*perc)) #random 10% sample of original data
 
sns.lmplot(x = "coach_price", y = "firstclass_price", data = flight_sub, line_kws={'color': 'black'}, lowess=True)
plt.show()
plt.clf()

## Task 5
# Inflight Meals
sns.histplot(flight, x = "coach_price", hue = flight.inflight_meal)
plt.show()
plt.clf()

# Inflight Entertainment
sns.histplot(flight, x = "coach_price", hue = flight.inflight_entertainment)
plt.show()
plt.clf()
 
# Inflight WiFi
sns.histplot(flight, x = "coach_price", hue = flight.inflight_wifi)
plt.show()
plt.clf()
#entertainment and wifi have the biggest impact on price

## Task 6
sns.lmplot(x = "hours", y = "passengers", data = flight_sub, x_jitter = 0.25, scatter_kws={"s": 5, "alpha":0.2}, fit_reg = False)
plt.show()
plt.clf()

## Task 7
sns.lmplot(x ='coach_price', y='firstclass_price', hue = 'weekend', data = flight_sub, fit_reg= False)
plt.show()
plt.clf()

'''We can see that on average, weekend tickets are more expensive than weekday tickets. However, based on this plot it seems like it’s easier to get a good deal on a first-class ticket on a weekday than on a weekend: the price difference between first-class and coach level tickets is larger on the weekend than on a weekday.'''

## Task 8
sns.boxplot(x = "day_of_week", y = "coach_price", hue = "redeye", data = flight)
plt.show()
plt.clf()
'''We can see more clearly that the difference between redeyes and non-redeyes is pretty much the same on any day of the week, though on average weekend flights cost more than weekday flights.'''



