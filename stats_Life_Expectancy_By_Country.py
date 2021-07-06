import codecademylib3_seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("country_data.csv")
#print(data.head(10))
life_expectancy=data['Life Expectancy']
life_exp_quartiles=np.quantile(life_expectancy,[0.25,0.50,0.75])
for i in life_exp_quartiles:
  print(i)

#plt.hist(life_expectancy)
#plt.show()

gdp=data['GDP']
median_gdp=np.quantile(gdp,0.5)
print(median_gdp)
low_gdp=data[data["GDP"]<=median_gdp]
high_gdp=data[data["GDP"]>median_gdp]
low_gdp_quartiles=np.quantile(low_gdp['Life Expectancy'],[0.25,0.5,0.75])
for i in low_gdp_quartiles:
  print(i)

high_gdp_quartiles=np.quantile(high_gdp['Life Expectancy'],[0.25,0.5,0.75])
for i in high_gdp_quartiles:
  print(i)

plt.hist(high_gdp["Life Expectancy"], alpha = 0.5, label = "High GDP")
plt.hist(low_gdp["Life Expectancy"], alpha = 0.5, label = "Low GDP")
plt.legend()
plt.show()
