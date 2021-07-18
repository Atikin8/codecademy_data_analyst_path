import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import codecademylib3

# load in the data
df = pd.read_csv("mushroom_data.csv")
print(df.head())

# list of all column headers
columns = df.columns.tolist()

for col in columns:
  #print(col)
  sns.countplot(df[col],order=df[col].value_counts(ascending=False).index) #shows bars in descending order
  plt.xticks(rotation=30,fontsize=10)
  plt.xlabel(col,fontsize=12)
  plt.title('{col} Value Counts'.format(col=col))
  plt.show()
  plt.clf()
