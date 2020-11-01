print("hello-10312020")
import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
df = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/cognexia_training_python/10232020/Data/Salary_Data.csv')
print(df.head())
# y = mc + c
# sal = m*exp + c
# y = b1x+b0
sns.scatterplot(df.Salary,df.YearsExperience)
print(df.info())
print(df.min())
print(df.max())
# plt.show()
X = df.iloc[:,:1].values
Y = df.iloc[:,1].values
print(X[:5])
print(Y[:5])
print(X.shape)
print(Y.shape)
print(Y[:5])
print(Y[:25])
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=5)
print(X_train.shape)
print(Y_train.shape)
print(X_test.shape)
print(Y_test.shape)

print(X_train)
print(Y_train)
print(X_test)
print(Y_test)

model = LinearRegression()
#y = mx + c
model.fit(X_train,Y_train)
LinearRegression()
print(model.coef_)
print(model.intercept_)
experience=20
salary = model.coef_*experience + model.intercept_
print(salary)