import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

request=requests.get('https://content.codecademy.com/courses/beautifulsoup/cacao/index.html')
webpage=request.content
soup=BeautifulSoup(webpage,'html.parser')
#print(soup)
rating_tags=soup.find_all(attrs={'class':'Rating'})
#print(rating_tags)
ratings=[]
for rating in rating_tags[1:]:
  r=rating.get_text()
  ratings.append(float(r))

#print(ratings)
plt.hist(ratings)
plt.show()
#company_tags=soup.find_all(attrs={'class':'Company'})
company_tags=soup.select('.Company')
#print(company_tags)
company=[]
for c in company_tags[1:]:
  comp=c.get_text()
  company.append(comp)
#print(company)
cacao_df=pd.DataFrame({"Company": company,"Rating": ratings})
#print(cacao_df)
top_10rating=cacao_df.groupby('Company')['Rating'].mean().nlargest(10)
#print(top_10rating)
cocoapercentage_tags=soup.select('.CocoaPercent')
cocoa_percent=[]
for cocoa in cocoapercentage_tags[1:]:
  coco=float(cocoa.get_text().strip("%"))
  cocoa_percent.append(coco)

#print(cocoa_percent)
percent_series=pd.Series(cocoa_percent)
cacao_df['Cocoa Percent']=percent_series
print(cacao_df)
plt.clf()
plt.scatter(cacao_df['Cocoa Percent'],cacao_df['Rating'])
z = np.polyfit(cacao_df['Cocoa Percent'], cacao_df['Rating'], 1)
line_function = np.poly1d(z)
plt.plot(cacao_df['Cocoa Percent'], line_function(cacao_df['Cocoa Percent']), "r--")
plt.show()

