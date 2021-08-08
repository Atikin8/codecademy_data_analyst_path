# import libraries
import codecademylib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

# load data
heart = pd.read_csv('heart_disease.csv')

print(heart.head())

sns.boxplot(heart['heart_disease'],heart['thalach'])
plt.show()
#Based on this plot, patients diagnosed with heart disease generally had a lower maximum heart rate during their exercise test
thalach_hd=heart['thalach'][heart['heart_disease']=='presence']
thalach_no_hd=heart['thalach'][heart['heart_disease']=='absence']
#print(thalach_no_hd)
mean_diff=np.mean(thalach_hd)-np.mean(thalach_no_hd)
median_diff=np.median(thalach_hd)-np.median(thalach_no_hd)
print('Thalach Mean Difference: ',mean_diff)
print('Thalach Median Difference: ',median_diff)

# run two-sample t-test
from scipy.stats import ttest_ind
tstat,pval=ttest_ind(thalach_hd, thalach_no_hd)
print('P-value for thalach two-sample t-test: ', pval)
#This is less than 0.05, so we “reject the null hypothesis” and conclude that there is a significant difference in thalach
#for people with heart disease compared to people without heart disease.

# investigating other quantitative variables
#age
plt.clf()
sns.boxplot(x=heart.heart_disease, y=heart.age)
plt.show()
age_hd=heart.age[heart.heart_disease =='presence']
age_no_hd=heart.age[heart.heart_disease =='absence']
mean_diff=np.mean(age_hd)-np.mean(age_no_hd)
print('`age` mean Difference: ', mean_diff)
med_diff = np.median(age_hd) - np.median(age_no_hd)
print('`age` median Difference: ', med_diff)
tstat, pval = ttest_ind(age_hd, age_no_hd)
print('p-value for `age` two-sample t-test: ', pval)

#trestbps
plt.clf()
sns.boxplot(x=heart.heart_disease, y=heart.trestbps)
plt.show()
trestbps_hd = heart.trestbps[heart.heart_disease == 'presence']
trestbps_no_hd = heart.trestbps[heart.heart_disease == 'absence']
mean_diff = np.mean(trestbps_hd) - np.mean(trestbps_no_hd)
print('`trestbps` mean Difference: ', mean_diff)
med_diff = np.median(trestbps_hd) - np.median(trestbps_no_hd)
print('`trestbps` median Difference: ', med_diff)
tstat, pval = ttest_ind(trestbps_hd, trestbps_no_hd)
print('p-value for `trestbps` two-sample t-test: ', pval)

#chol
plt.clf()
sns.boxplot(x=heart.heart_disease, y=heart.chol)
plt.show()
chol_hd = heart.chol[heart.heart_disease == 'presence']
chol_no_hd = heart.chol[heart.heart_disease == 'absence']
mean_diff = np.mean(chol_hd) - np.mean(chol_no_hd)
print('`chol` mean Difference: ', mean_diff)
med_diff = np.median(chol_hd) - np.median(chol_no_hd)
print('`chol` median Difference: ', med_diff)
tstat, pval = ttest_ind(chol_hd, chol_no_hd)
print('p-value for `chol` two-sample t-test: ', pval)

#Using a 0.05 significance threshold, both age (p = 8.955636917529706e-05) and trestbps (p = 0.008548268928594928) are significantly associated with heart disease.
#chol is not significantly associated with heart disease (p = 0.13914167020436527).

# box plot of `thalach` based on `cp`
plt.clf()
sns.boxplot(x=heart.cp, y=heart.thalach)
plt.show()

# save `thalach` based on `cp`
thalach_typical = heart.thalach[heart.cp == 'typical angina']
thalach_asymptom = heart.thalach[heart.cp == 'asymptomatic']
thalach_nonangin = heart.thalach[heart.cp == 'non-anginal pain']
thalach_atypical = heart.thalach[heart.cp == 'atypical angina']

# run ANOVA
from scipy.stats import f_oneway
Fstat, pval = f_oneway(thalach_typical, thalach_asymptom, thalach_nonangin, thalach_atypical)
print('p-value for ANOVA: ', pval)
#there is at least one pair of chest pain types (cp) for which people with those pain types have significantly different average max heart rates during exercise (thalach)

# run Tukey's range test
from statsmodels.stats.multicomp import pairwise_tukeyhsd
output = pairwise_tukeyhsd(heart.thalach, heart.cp)
print(output)
#For any pair where “Reject” is “True”, we conclude that people with those chest pain types have significantly different maximum heart rates during exercise

# contingency table of heart disease vs cp
Xtab = pd.crosstab(heart.cp, heart.heart_disease)
print(Xtab)

# run chi-square test
from scipy.stats import chi2_contingency
chi2, pval, dof, exp = chi2_contingency(Xtab)
print('p-value for chi-square test: ', pval)
#This is less than 0.05, so we can conclude that there is a significant association between these variables.


