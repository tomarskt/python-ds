print("Hello - 10242020")
import pandas as pd
import numpy as np
import seaborn as sbn
import matplotlib.pyplot as plt
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
titanic = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/cognexia_training_python/10232020/Data/titanic.csv',usecols=['PassengerId','Name','Age','Fare'])
print(titanic.tail(2))