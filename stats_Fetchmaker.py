# Import libraries
import numpy as np
import pandas as pd
import codecademylib3

# Import data
dogs = pd.read_csv('dog_data.csv')

# Inspect first few rows of data
print(dogs.head())

# Save the is_rescue column for whippets
#whippet_rescue=dogs[(dogs["breed"]=='whippet') & (dogs['is_rescue']==1)]
whippet_rescue=dogs["is_rescue"][dogs['breed']=='whippet']
#print(whippet_rescue)

# Calculate and print the number of whippet rescues
num_whippet_rescues=np.sum(whippet_rescue)
print("whippets rescued: ",num_whippet_rescues)

# Calculate and print the number of whippets
num_whippets=len(whippet_rescue)
print("total whippets in the sample: ",num_whippets)

# Run a binomial test 
from scipy.stats import binom_test
pval = binom_test(num_whippet_rescues, num_whippets, .08)
print(pval)

# Save the weights of whippets, terriers, and pitbulls
wt_whippets=dogs['weight'][dogs['breed']=='whippet']
wt_terriers = dogs.weight[dogs.breed == 'terrier']
wt_pitbulls = dogs.weight[dogs.breed == 'pitbull']

# Run an ANOVA 
from scipy.stats import f_oneway
fstat,pval =f_oneway(wt_whippets,wt_terriers,wt_pitbulls)
print(pval) #pval below 0.05, reject null hypothesis

# Subset to just whippets, terriers, and pitbulls
dogs_wtp=dogs[dogs.breed.isin(['whippet','terrier','pitbull'])]

# Run Tukey's Range Test
from statsmodels.stats.multicomp import pairwise_tukeyhsd
result = pairwise_tukeyhsd(dogs_wtp.weight, dogs_wtp.breed)
print(result)  #pitbul and terrier weight differently, and terrier and whippet too

# Subset to just poodles and shihtzus
dogs_ps=dogs[dogs.breed.isin(['poodle', 'shihtzu'])]

# Create a contingency table of color vs. breed
xtab = pd.crosstab(dogs_ps.color,dogs_ps.breed)
print(xtab)

# Run a Chi-Square Test
from scipy.stats import chi2_contingency
chi2, pval, dof, exp = chi2_contingency(xtab)
print(pval)  #there is no association between breed and color




