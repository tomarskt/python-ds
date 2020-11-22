print("11212020")
import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.datasets import load_boston
import warnings
warnings.filterwarnings('ignore')
# df = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/projects/cognixia/data/Churn_Modelling.csv')
# print(df.head())
# print(df.info())
# df.drop(['RowNumber','CustomerId','Surname'],axis=1,inplace=True)
# print(df.head())
# print(df.describe(percentiles=(0.5,0.7,0.8,0.9,0.95,0.99)))
# print(df.sort_values(by='Age',ascending=False))
# print(df.Gender.unique())
# print(df.Geography.unique())
# df.Gender=df.Gender.apply(lambda x: 1 if x=='Male' else 0)
# geo = pd.get_dummies(df.Geography,drop_first=True)
# print(geo) #get_dummies replace category with 0/1 or numerical
# df = pd.concat([df,geo],axis=1)
# print(df.drop('Geography',axis=1,inplace=True))
# print(df.info())
# x = df.drop('Exited',axis=1)
# print(x)
# y = df['Exited']
# print(y)
# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=142)
# print(x_train.head())

# from sklearn.preprocessing import StandardScaler
# sc = StandardScaler()
# x_train = sc.fit_transform(x_train)
# x_test = sc.transform(x_test)
# logitreg = LogisticRegression()
# logitreg.fit(x_train,y_train)
# y_pred=logitreg.predict(x_test)
# print(accuracy_score(y_test,y_pred))
# print(confusion_matrix(y_test,y_pred))
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

# df = pd.read_excel('/Users/stomar-n/001_sudhir_2020_nmac/projects/cognixia/data/abc-bank.xlsx')
# print(df.head)
# print(df.info)
# print(df.mean)
# print(df.mean(axis=0))
# print("Sum: ",df["9Profit"].sum()) 
# print("Mean: ",df["9Profit"].mean())
# print("Maximum: ",df["9Profit"].max())
# print("Minimum: ",df["9Profit"].min()) 
# df_online = df[df["9Online"]==0]
# df_offline=df[df["9Online"]==1]
# print(df_online.mean(axis=0))
# print(df_offline.mean(axis=0))
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
churn = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/projects/cognixia/data/churn_data.csv')
internet = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/projects/cognixia/data/internet_data.csv')
customer = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/projects/cognixia/data/customer_data.csv')
print(churn.head(2))
print(internet.head(2))
print(customer.head(2))
df = pd.merge(churn,customer,on='customerID')
print(df.head(2))
tel = pd.merge(df,internet,on='customerID')
print(tel.head(2))
print(tel.shape)
print(tel.describe())
print(tel.info())
tel.drop(['customerID'],axis=1,inplace=True)
print(pd.get_dummies(tel))
print(tel.columns)
for col in tel.columns:
    print(col, '-->\t\t',tel[col].unique)
vars = ['PhoneService','Churn','Partner','Dependents','PaperlessBilling']
def bin_map(x):
    return x.map({'Yes':1, 'No':0})
tel[vars]=tel[vars].apply(bin_map)
print(tel.head(2))

for col in tel.columns:
    # print(tel[col].dtype)
    if tel[col].dtype == 'O':
        print(col, '-->\t\t', tel[col].unique())
print(tel.info())
tel.gender = tel.gender.apply(lambda x:1 if x == 'Male' else 0)
vars = ['Contract','PaymentMethod','gender','InternetService']
d = pd.get_dummies(tel[vars],drop_first=True)
# pd.get_dummies(tel[vars],drop_first=True)
print(d)
tel = pd.concat([tel,d],axis=1)
tel.drop(vars,axis=1,inplace=True)

for col in tel.columns:
    if tel[col].dtype == 'O':
        print(col, '-->\t\t', tel[col].unique())

vars = ['OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies']
for col in vars:
    d = pd.get_dummies(tel[col],prefix=col)
    d.drop(col+'_No internet service', axis=1, inplace = True)
    tel = pd.concat([tel,d], axis=1)
tel.drop(vars,inplace=True, axis=1)
print(tel.head())

for col in tel.columns:
    if tel[col].dtype == 'O':
        print(col, '-->\t\t', tel[col].unique())

print(tel.info())

d = pd.get_dummies(tel['MultipleLines'],prefix='MultipleLines')
d.drop('MultipleLines_No phone service', inplace = True, axis=1)
tel = pd.concat([tel,d],axis=1)
tel.drop('MultipleLines',inplace=True,axis=1)

for col in tel.columns:
    if tel[col].dtype == 'O':
        print(col, '-->\t\t', tel[col].unique())
# tel.to_csv('/Users/stomar-n/001_sudhir_2020_nmac/projects/cognixia/data/tel.csv')
pd.to_numeric(tel['TotalCharges'],errors='coerce')
print(tel.info())
tel.dropna(inplace=True)
print(tel.info())
print(tel.head())
# //get x,y, train_test_split
x = tel.drop('Churn', axis=1)
y = tel['Churn']
print(x.columns)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.33,random_state=100)
print(x_train.head())
print(x_train.shape)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
vars = ['tenure','MonthlyCharges','TotalCharges']
# x_train[vars] = sc.fit_transform(x_train[vars])
# x_test[vars] = sc.transform(x_test[vars])
# print(x_test.head())
plt.figure(figsize=(10,10))
sns.heatmap(tel.corr(),annot=True)


import statsmodels.api as sm
logm1 = sm.GLM(y_train,sm.add_constant(x_train),family=sm.families.Binomial())
print(logm1)
print(logm1.fit().summary())

# logreg = LogisticRegression()
# from sklearn.feature_selection import RFE
# rfe = RFE(logreg,15)
# rfe = rfe.fit(x_train,y_train)
# print(rfe_support_)