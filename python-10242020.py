print("Hello - 10242020")
import pandas as pd
import numpy as np
import seaborn as sbn
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