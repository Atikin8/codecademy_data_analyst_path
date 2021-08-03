# import libraries
import codecademylib3
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp
from scipy.stats import binom_test

# load data
heart = pd.read_csv('heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']
# get cholesterol levels for patients with heart disease
chol_hd=yes_hd['chol']
# calculate mean cholesterol level for patients with hd
print(np.mean(chol_hd))
# compare to cut-off for high cholesterol
tstat, pval = ttest_1samp(chol_hd, 240)
print(pval/2)
# p-value is less than 0.05, which suggests that heart disease patients have an average cholesterol level significantly higher than 240 mg/dl

#repeat steps for no heart disease patients
no_chol_hd=no_hd['chol']
print(np.mean(no_chol_hd))
tstat, pval = ttest_1samp(no_chol_hd, 240)
print(pval/2)
# p-value is greater than 0.05, which suggests that patients without heart disease have an average cholesterol level equal to 240 mg/dl

num_patients=len(heart)
print(num_patients)
#get num of patients with fasting blood suger above 120
highfbs_patients=heart[heart['fbs']==1]
num_highfbs_patients=len(highfbs_patients)
print(num_highfbs_patients)

# calculate 8% of sample size
print(0.08*num_patients)

# run binomial test
pval=binom_test(num_highfbs_patients, num_patients, .08, alternative='greater')
print(pval)
#p-value is less than 0.05, indicating that this sample likely comes from a population where more than 8% of people have fbs > 120 mg/dl.

