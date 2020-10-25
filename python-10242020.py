print("Hello - 10242020")
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
d = {'A': [1,2,np.nan], 'B': [4,np.nan,np.nan], 'C': [7,8,9]}
df = pd.DataFrame(d)
print(df)
titanic = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/cognexia_training_python/10232020/Data/titanic.csv')
print(titanic.head)
print(len(titanic))
print(len(titanic.columns))
print(titanic.info)
print(titanic.tail)
print(titanic.tail(2))
print(titanic.head(2))
d={'Day':[1,2,3,4,5,6,7],'Visitors':[300,400,500,600,700,800],'Bounce_rate':[100,50,20,40,10,30,70]}
# pd.DataFrame(d)
titanic.drop('Cabin',axis=1)
print(titanic.head)
titanic.drop('Cabin',axis=1,inplace=True)
# titanic.drop('Cabin',axis='columns',inplace=True)
print(titanic.head)
# titanic.drop('Cabin',axis='rows',inplace=True)

print(titanic.tail(2))
print(titanic.drop(['PassengerId','Survived','Name'],axis=1, inplace=True))
print(titanic.tail(2))
titanic = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/cognexia_training_python/10232020/Data/titanic.csv',usecols=['PassengerId','Name','Age','Fare'])
print(titanic.tail(2))
#Axis = 0 = Rows
#Axis = 1 = Columns
titanic_orig = titanic.copy()
print(titanic_orig.head(2))
d={'Day':[1,2,3,4,5,6,7],'Visitors':[300,400,500,600,700,800,900],'Bounce_rate':[100,50,20,40,10,30,70]}
df=pd.DataFrame(d)
print(df)
df.to_excel('/Users/stomar-n/001_sudhir_2020_nmac/cognexia_training_python/10232020/df_to_excel.xlsx')
print(df.dropna())
print(df.describe())
print(titanic.describe())
print(titanic.info())
titanic = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/cognexia_training_python/10232020/Data/titanic.csv')
print(titanic.head)
print(titanic.columns)
print(titanic[titanic['Age']>70])
print(titanic[(titanic['Age']>60) & (titanic['Sex']=='female')])
print(titanic.head(2))
titanic['Age'] = titanic['Age'] +2
print(titanic.head(2))
print(titanic[titanic['Age']<3])
df1 = titanic[titanic['Age']<3]
print(df1.head(3))
df1['Age'] +=5
print(df1.head(3))
print(titanic[titanic['Age']<3])
print(titanic.Name)
print(titanic['Name'].str.upper())
print(titanic['Name'].str.split(',')[0])
print(titanic['Name'].str.split(',')[1])
print(titanic.Name.str.split(',',expand=True)[0])
print(titanic.Name.str.split(',',expand=True)[1])
print(type(titanic.Name.str.split(',',expand=True)))
titanic['FName']=titanic.Name.str.split(',',expand=True)[1]
titanic['LName']=titanic.Name.str.split(',',expand=True)[0]
# print
titanic.drop('Name',axis=1,inplace=True)
print(titanic.head(5))
# titanic['FName']=titanic['Name'].str.split(',')[1]
# print(titanic['FName'])
print(titanic.iloc[4])
print(titanic.iloc[4]['PassengerId'])
print(titanic.iloc[4]['FName'])
# print(titanic.iloc[4]['FName'])
print(titanic.iloc[1:4,1:5])
print(titanic.iloc[1:4][['Survived','Pclass','FName']])
print(titanic.iloc[1:4][['Survived','Pclass','FName']])
print(titanic.values.T)

d={'Day':[1,2,3,4,5,6,7],'Visitors':[300,400,500,600,700,800,900],'Bounce_rate':[100,50,20,40,10,30,70]}
df=pd.DataFrame(d)
print(df)
print(type(df['Visitors']))
print(type(df[['Visitors']]))
print(df['Visitors']) #Series
print(df[['Visitors']]) #DataFrame
print(df[['Visitors']].iloc[0:5])
# groupby
#sort_values()
print(df.groupby('Visitors'))
print(df.sort_values('Bounce_rate'))

# grp = df_5.groupby(by=['subject','names']).mean()['marks']
# df2.sort_values('country',ascending=False,inplace= True)

data1={'Day':[1,2,3,4,5,6,7], 'Visitors':[300,400,230,230,400,600,450],'Bounce_rate':[100,50,20,40,10,30,70]} 
data2={'Day':[1,2,3,4,5,6,7], 'Visitors':[265,401,290,230,290,505,400],'Bounce_rate':[101,60,30,30,20,20,60]}
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
print(df1)
print(df2)

df1=pd.DataFrame(data1,index=[10,20,30,40,50,60,70])
df2=pd.DataFrame(data2,index=[10,20,30,40,50,60,70])
print(df1)
print(df2)

data1={'Day':[1,2,3,4,5,6,7], 'Visitors':[300,400,230,230,400,600,450],'Bounce_rate':[100,50,20,40,10,30,70]} 
data2={'Day':[1,2,3,4,5,6,7], 'Visitors':[265,401,290,230,290,505,450],'Bounce_rate':[101,60,20,30,20,20,60]} 
df1 = pd.DataFrame(data1, index=[10,20,30,40,50,60,70]) 
df2 = pd.DataFrame(data2, index=[10,20,30,40,50,60,70])

# df1=pd.DataFrame(data1,index=list(range(1000,10000,10)))
# df2=pd.DataFrame(data2,index=list(range(1000,10000,10)))
# print(df1)
# print(df2)

print(pd.merge(df1,df2,on=['Visitors']))
print(pd.merge(df1,df2,on=['Day']))
print(pd.merge(df1,df2,on=['Bounce_rate']))
print(pd.merge(df1,df2,on=['Day','Bounce_rate']))
print(pd.merge(df1,df2,on=['Day','Bounce_rate'],how='inner'))

customer = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/cognexia_training_python/10232020/Data/customer_data.csv')

internet = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/cognexia_training_python/10232020/Data/internet_data.csv')
print(customer.head)
print(internet.head)
new_df = pd.merge(customer,internet,on=['customerID'])
print(new_df)

print(titanic.sort_values('Age',ascending=False))
print(titanic.sort_values('Fare',ascending=False))
data = {'company': ['Google', 'Microsoft', 'Google', 'Amazon', 'Amazon', 'Google'], 
'sales': [233, 453, 342, 644, 255, 300], 
'person': ['Aakash', 'Mohan', 'John', 'Alexandre', 'Fred', 'Muralidhar']} 
df = pd.DataFrame(data) 
print(df)
print(df.groupby(by='company'))
g = df.groupby(by='company')
print(g)
print(list(g))
for n,df in g:
    print(n)
    print('*************')
    print(df)
    print()

for n,df in g:
    if n == 'Google':
        print(df['sales'].mean())
    # print(n)
    # print('*************')
    # print(df)
    # print()
#groupby is a generator object
a=np.array([911,2323,3434,4000,5677,1200,3210,4490,5400,6755,699,1539,2399,4200,5599,1239,2500,4211,5388,6877])
print(a)
# plt.figure(figsize=(8,5))
# sns.barplot(list(range(len(a))),a)
# plt.show()
# # sns.barplot(list(range(len(a))),a)
# plt.plot([2,3,6,4,5,4,6,8,9])
# plt.plot([3,5,4,6,4,2,7,4,20,30,100,10,1,2,3,4,5,6,7])
# plt.show()
# titanic.Sex.value_counts().plot(kind='bar')
# plt.show()
# # sns.barplot(['male','female'],titanic.Sex,titanic.Sex.value_counts())
# # plt.show()
gas = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/cognexia_training_python/10232020/Data/gas_prices.csv')
print(gas.head(2))
# plt.plot(gas['Year'],gas['Canada'],'b-')
# plt.show()
# plt.figure(figsize=(12,7)) 
# plt.plot(gas['Year'], gas['Canada'], 'bo-.',markersize='green',) 
# plt.title('Gas price for Canada') 
# plt.xlabel('Year') 
# plt.ylabel('Gas price in USD') 
# plt.show()

plt.figure(figsize=(12,7)) 
plt.plot(gas['Year'], gas['Canada'], 'bo-.', markersize=8, markerfacecolor='green', markeredgecolor='red') 
plt.plot(gas['Year'], gas['France'], 'bo-.', markersize=8, markerfacecolor='green', markeredgecolor='red') 
plt.title('Gas price for Canada') 
plt.xlabel('Year') 
plt.ylabel('Gas price in USD') 
plt.savefig('/Users/stomar-n/001_sudhir_2020_nmac/cognexia_training_python/10232020/gas.jpeg') 
plt.show()

print(gas.columns)
plt.figure(figsize=(12,7))
for c in gas.columns[1:]:
    plt.plot(gas['Year'],gas[c])
plt.legend(gas.columns[1:])
plt.show()