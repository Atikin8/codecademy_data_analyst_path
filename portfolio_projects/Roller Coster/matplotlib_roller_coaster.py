# Import internal library
import codecademylib3
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
# load rankings data
wood=pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
print(wood.head())
# load rankings data
steel=pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
print(steel.head())
# Create a function to plot rankings over time for 1 roller coaster
def coaster_ranking(name,park,dataset):
  plt.clf()
  subset=dataset[(dataset['Name']==name) & (dataset['Park']==park)].reset_index(drop=True)
  fig, ax=plt.subplots()
  ax.plot(subset['Year of Rank'],subset['Rank'])
  ax.invert_yaxis()
  ax.set_xticks(subset['Year of Rank'].values)
  ax.set_yticks(subset['Rank'].values)
  plt.xlabel('Year')
  plt.ylabel('Rank')
  plt.title("{name}'s {park} Rank by Year".format(name=name,park=park))
  plt.show()
# Create a plot of El Toro ranking over time
coaster_ranking('El Toro','Six Flags Great Adventure',wood)
# function to plot rankings over time for 2 roller coasters
def two_coaster_ranking(name1,park1,name2,park2,dataset):
  plt.clf()
  subset1=dataset[(dataset['Name']==name1) & (dataset['Park']==park1)].reset_index(drop=True)
  subset2=dataset[(dataset['Name']==name2) & (dataset['Park']==park2)].reset_index(drop=True)
  fig, ax=plt.subplots()
  ax.plot(subset1['Year of Rank'],subset1['Rank'],label=park1)
  ax.plot(subset2['Year of Rank'],subset2['Rank'],label=park2)
  ax.invert_yaxis()
  ax.set_xticks(subset1['Year of Rank'].values)
  ax.set_yticks(subset1['Rank'].values)
  plt.xlabel('Year')
  plt.ylabel('Rank')
  plt.title("{park1} vs {park2} Rank by Year".format(park1=park1,park2=park2))
  plt.legend()
  plt.show()
# Create a plot of El Toro and Boulder dash hurricanes
two_coaster_ranking('El Toro','Six Flags Great Adventure','Boulder Dash','Lake Compounce',wood)
# Create a function to plot top n rankings over time
def top_n_parks(n,dataset):
  plt.clf()
  subset=dataset[dataset['Rank']<=n]
  fig,ax=plt.subplots(figsize=(10,10))
  for name in set(subset['Name']):
    one_park=subset[subset['Name']==name]
    ax.plot(one_park['Year of Rank'],one_park['Rank'],label=name)
  ax.invert_yaxis()
  ax.set_xticks(subset['Year of Rank'].values)
  ax.set_yticks(subset['Rank'].values)
  plt.xlabel('Year')
  plt.ylabel('Rank')
  plt.title("Top {n}  Coasters by Year".format(n=n))
  plt.legend(loc=4)
  plt.show()
# Create a plot of top n rankings over time
top_n_parks(5,wood)
# load roller coaster data
coasters=pd.read_csv("roller_coasters.csv")
print(coasters.head())
# Create a function to plot histogram of column values
def histo(dataset,column):
  plt.clf()
  plt.hist(dataset[column].dropna())
  plt.title("Histogram of {}".format(column))
  plt.xlabel(column)
  plt.ylabel('count')
  plt.show()
# Create histogram of roller coaster speed
histo(coasters,'speed')
# Create histogram of roller coaster length
histo(coasters,'length')
# Create a function to plot inversions by coaster at park
def barchart_inv(dataset,park_name):
  plt.clf()
  inversions=dataset[dataset['park']==park_name]
  inversions=inversions.sort_values('num_inversions',ascending=False)
  names=inversions['name']
  counts=inversions['num_inversions']
  plt.bar(range(len(names)),counts)
  ax=plt.subplot()
  ax.set_xticks(range(len(names)))
  ax.set_xticklabels(names,rotation=90)
  plt.title("# of Inversions per Coaster")
  plt.xlabel("Coaster")
  plt.ylabel("# of Inversions")
  plt.show()
# Create barplot of inversions by roller coasters
barchart_inv(coasters,'Parc Asterix')

# Create a function to plot a pie chart of status.operating
def status_piechart(dataset):
  operating=dataset[dataset['status']=='status.operating']
  closed=dataset[dataset['status']=='status.closed.definitely']
  plt.clf()
  plt.pie([len(operating),len(closed)],autopct='%0.1f%%',labels=['Operating','Closed'])
  plt.title("Operating vs Closed Coasters")
  plt.legend()
  plt.axis('equal')
  plt.show()
# Create pie chart of roller coasters
status_piechart(coasters)
# Create a function to plot scatter of any two columns
def scatter(dataset,col1,col2):
  plt.clf()
  plt.scatter(dataset[col1],dataset[col2])
  plt.xlabel(col1)
  plt.ylabel(col2)
  plt.title('Scatter Plot {x} vs {y}'.format(x=col1,y=col2))
  plt.show()

scatter(coasters,'speed','length')


