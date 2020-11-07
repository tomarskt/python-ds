print("11062020-2-ABCBank")

import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.datasets import load_boston
# boston = load_boston()
# print(boston.DESCR)
# df = pd.DataFrame(boston.data)
# # print(df.head)
# print(boston.feature_names)
# df.columns = boston.feature_names
# print(df.head)
# df['PRICE']=boston.target
# print(df.head)
# print(boston)
# x = df.iloc[:,:-1].values
# y=df.iloc[:,-1].values
# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
# x=boston.data
# y=boston.target
# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
# boston = load_boston()
# x_train,x_test,y_train,y_test=train_test_split(boston.data,boston.target,test_size=0.2,random_state=42)
# print(x_train)
# regressor = LinearRegression()
# regressor.fit(x_train,y_train)
# print("*******************coef_")
# print(regressor.coef_)
# print("*******************intercept_")
# print(regressor.intercept_)
# y_pred=regressor.predict(x_test)
# print(y_pred)
# print(np.sqrt(mean_squared_error(y_test,y_pred)))

# plt.figure(figsize=(10,10))
# plt.scatter(x_train,y_train,color='red')
# plt.plot(x_train,model.predict(x_train),color='blue')
# plt.scatter(x_test,y_test,color='green')
# plt.plot(y_pred)
# plt.show()

df = pd.read_excel('/Users/stomar-n/001_sudhir_2020_nmac/projects/cognixia/data/abc-bank.xlsx')
print(df.head)
print(df.info)
print(df.mean)
print(df.mean(axis=0))
print("Sum: ",df["9Profit"].sum()) 
print("Mean: ",df["9Profit"].mean())
print("Maximum: ",df["9Profit"].max())
print("Minimum: ",df["9Profit"].min()) 
df_online = df[df["9Online"]==0]
df_offline=df[df["9Online"]==1]
print(df_online.mean(axis=0))
print(df_offline.mean(axis=0))
# print(boston.)
# df = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/cognexia_training_python/10232020/Data/Salary_Data.csv')
# print(df.head())
# # y = mc + c
# # sal = m*exp + c
# # y = b1x+b0
# sns.scatterplot(df.Salary,df.YearsExperience)
# print(df.info())
# print(df.min())
# print(df.max())
# # plt.show()
# X = df.iloc[:,:1].values
# Y = df.iloc[:,1].values
# print(X[:5])
# print(Y[:5])
# print(X.shape)
# print(Y.shape)
# print(Y[:5])
# print(Y[:25])
# X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=5)
# print(X_train.shape)
# print(Y_train.shape)
# print(X_test.shape)
# print(Y_test.shape)

# print(X_train)
# print(Y_train)
# print(X_test)
# print(Y_test)

# model = LinearRegression()
# #y = mx + c
# model.fit(X_train,Y_train)
# LinearRegression()
# print(model.coef_)
# print(model.intercept_)
# experience=20
# salary = model.coef_*experience + model.intercept_
# print(salary)
# print(model.predict(X_test))
# print(Y_test)
# print(model.predict(np.array([[5.7]])))
# new_data=np.array([[2.5],[8],[17],[19]])
# print(model.predict(new_data))

# #RMSE
# #Pilgrim Bank...Case Study--
# plt.figure(figsize=(10,10))
# plt.scatter(X_train,Y_train,color='red')
# # plt.show()
# plt.plot(X_train,model.predict(X_train),color='blue')
# plt.scatter(X_test,Y_test,color='green')
# plt.show()
# from sklearn.metrics import mean_squared_error
# Y_pred=model.predict(X_test)
# print(np.sqrt(mean_squared_error(Y_test,Y_pred)))