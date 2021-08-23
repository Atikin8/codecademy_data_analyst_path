import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df=pd.read_csv('WorldCupMatches.csv')
#print(df.head())
df['Total Goals']=df['Home Team Goals']+df['Away Team Goals']
print(df.head())

sns.set_style('whitegrid')
sns.set_context('notebook',font_scale=1.25)
f,ax=plt.subplots(figsize=(12,7))
ax=sns.barplot(x=df['Year'],y=df['Total Goals'])
ax.set_title('AVG Goals Over the Years')
plt.show()

df_goals=pd.read_csv('goals.csv')
print(df_goals.head())
f,ax2=plt.subplots(figsize=(12,7))
ax=sns.boxplot(x=df_goals['year'],y=df_goals['goals'],palette='Spectral')
ax2.set_title("Goals Boxplot")
plt.show()
