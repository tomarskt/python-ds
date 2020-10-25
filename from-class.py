# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 10:58:15 2018

@author: Hemant Rathore
"""



'''
Data Analysis using Pandas DataFrame
'''


import numpy as np

import pandas as pd




#How to create Data Frame Using dectionary

sid =[1,2,3,4]

name=['alex','bella','john','joe']

year= [2001,2002,2003,2004]



df2=pd.DataFrame({'id':sid,'name':name,'year':year})

df2

df2.info()


# Accessing DF elements


# Accessing columns



print(df2)


df2['id']

df2['name']


df2.id

df2.name



df2[['id','name']]



# Accessing Records


df2[0:1]

df2[1:3]

df2[:2]

df2[1:]



# Accessing Columns and records together


dataframe[row_index][[col_names]]

df2[0:2]['name']

df2[0:2][['id','name']]



## using iloc


df2.iloc[0]


df2.iloc[1:3]


df2.iloc[[0],[0]]


df2.iloc[[0,1,3],[0,1]]


df2.iloc[1:3,[0,1]]


df2.iloc[[0,1],1:3]


df2.iloc[1:3,1:3]




## Modifying Structure & Data

## Adding a new column

country =  ['IND','US','EUR','AUS']

country

df2['country'] = country


df2=df2.assign(test=['1','2','3','4'])


## Dropping a column


df2.drop('test',axis=1)


df2.drop('test',axis=1,inplace=True)

df2



## adding a row


df0 = pd.DataFrame({'id':[5],'name':['new'],'year':[2018],'country':['a']})


df2 = df2.append(df0,ignore_index=True)



## Dropping a row

df2

df2.drop(3,axis=0,inplace=True)

df2.reset_index(drop=True,inplace=True)


df2


## Finding duplicate records

df2.duplicated()


df2

df2.drop_duplicates(inplace=True)

df2



# Sorting the records


df2


df2.sort_values('country')

df2.sort_values('country',ascending=False,inplace= True)




## Conditional data filtering


# select col from table where col=123


# table[(where)][[select]]


# df2[where][select]


df2

df2[df2.id > 2]

df2[df2.id >2 ]['name']

df2[df2.id >2 ][['name','country']]


df2[(df2.id != 2) & (df2.year >= 2003)][['name','country']]


df2[(df2.id >2) | (df2.year >= 2001)][['name','country']]

df2





## Merging/joining dataframes

# Inner join


df_1=pd.DataFrame({'id':[1,2,3],'name':['alex','bella','john'],'year':[2001,2002,2003]})
df_1

df_2=pd.DataFrame({'id':[1,2,4], 'city':['A',' B','C'],'pin':[1002002,1002003,1002001]})
df_2


df_merge = pd.merge(df_1,df_2 ,on='id')

df_merge


# outer joins


pd.merge(df_1,df_2,how='left',on='id')

pd.merge(df_1,df_2,how='right',on='id')

pd.merge(df_1,df_2,how='outer',on='id')


## Rename Columns

df_merge.columns[0] = ['ID', 'SName', 'year', 'city', 'pin']

df_merge.rename(columns={'ID':'SID'})


# DataFrames Binding (union)

# Row wise

df_1

df_3=pd.DataFrame({'id':[4,5,6],'name':['alex1','bella1','john1'],'year':[2001,2002,2003]})

df_3


pd.concat([df_1,df_3],axis=0)



## Data Aggregation


df_5 = pd.DataFrame({'id':[1,2,3,4,5],'names':['A','B','C','D','E'],'marks':[87,89,89,72,92],'subject':['S1','S2','S2','S1','S1']})

df_5

df_5.marks.mean()

df_5.marks.std()

df_5.marks.sum()

df_5.marks.min()

df_5.marks.max()

df_5.marks.var()

df_5.marks.median()

df_5.marks.mode()



# select subject,avg(marks) from student group by subject



# Group by

grp = df_5.groupby('subject')

grp.mean()

grp.mean()['marks']

grp.std()['marks']



grp = df_5.groupby(by=['subject','names']).mean()['marks']





## Importing data from file



Data = pd.read_csv("D:/Data Science Training/Data/Credit-Scoring-Clean.csv")

Data = pd.read_csv("D:/Data Science Training/Data/Credit-Scoring-Clean.csv",sep=';')


Data.info()

# Analyzing the dataframe


Data.info()

Data.describe()

Data.shape

Data.columns

Data.count()

Data.head(10)

Data.tail(10)


# Sampling

Data.sample(10)

Data.sample(frac=.01)


# writing to file


Data.to_csv("D:/Data Science Training/Data/new_file.csv",index=False)




# Using Excel files

data_1 = pd.read_excel("D:/Data Science Training/Data/Credit-Scoring-Clean.xlsx",sheet_name='Credit-Scoring-Clean')

data_1

data_1.to_excel("D:/Data Science Training/Data/new_file.xls")




## Connecting to Oracle database and reading data from table



from sqlalchemy import create_engine


conn = create_engine('oracle+cx_oracle://hemant:password@127.0.0.1:1521/?service_name=xe')


res=pd.read_sql_table('sales', conn)


res = pd.read_sql_query('select * from sales where product_type=\'Eyewear\' and product=\'Bella\'',conn)


# exporting Dataframe to table

res.to_sql('sales_result', conn, if_exists='replace')






## Some Inbuild Pandas Visualizations



res.plot()

res.revenue.plot()

res.revenue.hist()

res.revenue.plot.bar()

res.revenue.plot.box()

res.revenue.plot.kde()






'''
Data Visualization using Matplotlib
'''



import matplotlib.pyplot as plt

import numpy as np


## Using plot function

# Generate x, y coordinates


x = np.linspace(start = 0, stop = 20, num = 20)

x

y = np.linspace(start = 0, stop = 20, num = 20)+ np.random.randn(20)

y




# Draw the Plot


plt.plot(x, y)



# Some customizations


plt.plot(x, y, color='green', linestyle='--', marker='^')


plt.plot(x, y, color='green', marker='o',linestyle='')


# using fmt

plt.plot(x,y,'^-r')



# More customization

plt.plot(x, y, color='green', linestyle='solid', marker='o',
         markerfacecolor='red', markersize=10,linewidth=3,alpha=0.7)

plt.xlabel('X')

plt.ylabel('Y')

plt.title('Title')




## Using subplots function



x1 = np.linspace(start = 0, stop = 20, num = 20)
y1 = np.linspace(start = 0, stop = 20, num = 20)+ np.random.randn(20)


x2 = np.linspace(start = 0, stop = 20, num = 20)
y2 = np.linspace(start = 0, stop = 20, num = 20)+ np.random.randn(20)



fig,axes = plt.subplots()

axes.plot(x,y,label='Fund 1')
axes.plot(x1,y1,label='Fund 2')
axes.plot(x2,y2,label='Fund 3')

axes.legend()




# It allows you to have multiple subplots too

fig,axes = plt.subplots(nrows=1,ncols=2,figsize=(10,5))

axes[0].plot(x,y)
axes[1].plot(x1,y1,linestyle='', color='green',marker='o')

axes[1].set_title('Title 1')
axes[1].set_xlabel('X1')
axes[1].set_ylabel('Y1')
axes[1].grid(True)

fig.suptitle('Main-heading')


# saving the plot to file

fig.savefig('name.pdf',dpi=200)



# Different Type of EDA Approaches

# EDA - Univariate Analysis



## Histogram


z= (x-mu)/sigma

x = z*sigma + mu



Salary = np.random.randn(10000)*2000 + 25000


fig,axes = plt.subplots(figsize=(10,10))

axes.hist(Salary,rwidth=0.9,color='g',bins=50)



## Box plot


fig,axes = plt.subplots(figsize=(10,10))

axes.boxplot(Salary,labels=['Salary'],patch_artist=True)




# EDA - Bi-variate Analysis

## Scatter Plot

Salary = np.random.randn(100)*2000 + 25000
Exp = np.random.randn(100)*3 + 9


fig,axes = plt.subplots(figsize=(10,10))

axes.scatter(Exp, Salary)
axes.set_xlabel('Exp')
axes.set_ylabel('Salary')




## Sactter Plot - Adding more information


size = np.random.randn(100)*5+100
years = np.random.randn(100)*1+10

ctype = np.random.choice([0,1], size=100, replace=True)
Revenue = (np.random.rand(100)*30)**2


fig,axes = plt.subplots(figsize=(8,8))
scatter=axes.scatter(years,size,s=Revenue,c=ctype,alpha=0.7)

legend = axes.legend(*scatter.legend_elements(),loc="top left", title="ctype")
axes.add_artist(legend)

axes.set_xlabel('years')
axes.set_ylabel('size')




https://matplotlib.org/tutorials/index.html
