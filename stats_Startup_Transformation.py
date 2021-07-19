import codecademylib3
from sklearn import preprocessing
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# load in financial data
data = pd.read_csv('financial_data.csv')

# code goes here
print(data.head(10))
month=data['Month']
revenue=data['Revenue']
expenses=data['Expenses']

plt.plot(month,revenue)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Revenue')
plt.show()
plt.clf()
plt.plot(month,expenses)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Expenses')
plt.show()

expenses=pd.read_csv('expenses.csv')
print(expenses.head(10))
expense_cat=expenses['Expense']
proportions=expenses['Proportion']
plt.clf()
plt.pie(proportions,labels=expense_cat)
plt.axis("Equal")
plt.tight_layout()
plt.show()
plt.clf()

expense_categories=['Salaries','Advertising','Office Rent','Other']
proportions=[0.62,0.15,0.15,0.08]
plt.clf()
plt.pie(proportions,labels=expense_categories)
plt.title('Expense Categories')
plt.axis('Equal')
plt.tight_layout()
plt.show()
plt.clf()
expense_cut='Salaries'

employees=pd.read_csv('employees.csv')
print(employees.head())
sorted_productivity=employees.sort_values(by=['Productivity'])
print(sorted_productivity.head(10))
employees_cut=sorted_productivity[:100]
#print(employees_cut)
transformation = 'standardization'
commute_times=employees['Commute Time']
commute_times_log=np.log(commute_times)
print(commute_times.describe())

plt.hist(commute_times)
plt.title('Histogram of Commute Time')
plt.xlabel("Commute Time")
plt.ylabel("Frequency")
plt.show()
plt.clf()
plt.hist(commute_times_log)
plt.title('Histogram of Log of Commute Time')
plt.xlabel("Commute Time")
plt.ylabel("Frequency")
plt.show()


