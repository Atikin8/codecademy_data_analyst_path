# Import libraries
import pandas as pd
import numpy as np

# Load datasets
lifespans = pd.read_csv('familiar_lifespan.csv')
iron = pd.read_csv('familiar_iron.csv')
# Print lifespan data
print(lifespans.head())

# Save lifespans for vein pack subscribers
vein_pack_lifespans=lifespans['lifespan'][lifespans['pack']=='vein']
#print(vein_pack_lifespans)

# Calculate average lifespan for vein pack
print("Average lifespan for Vein Pack: ",np.mean(vein_pack_lifespans))

# Run one-sample t-test
from scipy.stats import ttest_1samp
tstat,pval =ttest_1samp(vein_pack_lifespans, 73)
print(pval)
#we conclude that the average lifespan of Vein Pack subscribers IS significantly different from 73 years.


# Save lifespans for artery pack subscribers
artery_pack_lifespans = lifespans.lifespan[lifespans.pack=='artery']

# Calculate artery pack life spans
print("Average Artery lifespan: ",np.mean(artery_pack_lifespans))

# Run two-sample t-test
from scipy.stats import ttest_ind
tstat, pval = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
print(pval)

#average lifespan of Vein Pack subscribers not significantly different from the average lifespan of an Artery Pack subscriber.

# Inspect first 5 rows of iron dataset
print(iron.head())

# Create contingency table
xtab = pd.crosstab(iron.pack, iron.iron)
print(xtab)

# Run Chi-Square test
from scipy.stats import chi2_contingency
chi2, pval, dof, exp = chi2_contingency(xtab)
print(pval)
# we conclude that there IS a significant association between pack and iron level.

