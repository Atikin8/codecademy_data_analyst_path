# Import libraries
import codecademylib3
import pandas as pd
import numpy as np

# Read in the `clicks.csv` file as `abdata`
abdata = pd.read_csv('clicks.csv')

# Inspect the dataframe
print(abdata.head())
# Create a contingency table with pd.crosstab
xtab=pd.crosstab(abdata['group'],abdata['is_purchase'])
print(xtab)
# Import chi2_contingency module and calculate p-value
from scipy.stats import chi2_contingency
chi2, pval, dof, expected = chi2_contingency(xtab)
print(pval)
#p-value is less than 0.05 and we can conclude that there is a
#significant difference in the purchase rate for groups A, B, and C

# Calculate and print the number of visits
num_visits = len(abdata)
print("Number of visits: ",num_visits)
# Calculate the purchase rate needed at 0.99
num_sales_needed_099=1000/0.99
print("# of $0.99 sales to breakeven: ",num_sales_needed_099)
# Print the purchase rate needed at 0.99
p_sales_needed_099 = num_sales_needed_099/num_visits
print("Purchase rate of $0.99 sales to breakeven: ", p_sales_needed_099)
# Calculate the purchase rate needed at 1.99
num_sales_needed_199 = 1000/1.99
p_sales_needed_199 = num_sales_needed_199/num_visits
# Print the purchase rate needed at 1.99
print("Purchase rate of $1.99 sales to breakeven: ", p_sales_needed_199)
# Calculate the purchase rate needed at 4.99
num_sales_needed_499 = 1000/4.99
p_sales_needed_499 = num_sales_needed_499/num_visits
# Print the purchase rate needed at 4.99
print("Purchase rate of $4.99 sales to breakeven: ",
p_sales_needed_499)
# Calculate samp size & sales for 0.99 price point
samp_size_099 = np.sum(abdata.group == 'A')
sales_099 = np.sum((abdata.group == 'A') & (abdata.is_purchase == 'Yes'))
# Print samp size & sales for 0.99 price point
print(samp_size_099)
print(sales_099)
# Import the binom_test module and Calculate the p-value for Group A
from scipy.stats import binom_test
pvalueA = binom_test(sales_099, n=samp_size_099, p=p_sales_needed_099, alternative='greater')
# Print the p-value for Group A
print(pvalueA) # p-value is above 0.05, so observed purchase rate is not significatily greater
