import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

import warnings
warnings.filterwarnings('ignore')

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/projects/cognixia/data/AdultIncome.csv')
print(df.head())
print(df.IncomeClass.unique())
print(df.info())
print(df.isnull().sum())
print(len(df.drop_duplicates()))
print(df.duplicated())
print(df[(df.age==27) & (df.education==' HS-grad') & (df['marital status'] == ' Never-married')])
print(df.education.unique())
df.drop_duplicates(inplace=True)
print(df.info())
print(pd.get_dummies(df.wc))
print(pd.get_dummies(df,drop_first=True))
df = pd.get_dummies(df,drop_first=True)
print(df.info())
x = df.iloc[:, :-1]
print(x)
y = df['IncomeClass_ >50K']
print(y)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=42)
dt = DecisionTreeClassifier()
rf = RandomForestClassifier(n_estimators=100)
dt.fit(x_train,y_train)
rf.fit(x_train,y_train)
y_pred_dt = dt.predict(x_test)
y_pred_rf = rf.predict(x_test)
print(accuracy_score(y_test,y_pred_dt))
print(accuracy_score(y_test,y_pred_rf))
print(confusion_matrix(y_test,y_pred_dt))
print(confusion_matrix(y_test,y_pred_rf))
# churn = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/projects/cognixia/data/churn_data.csv')
# internet = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/projects/cognixia/data/internet_data.csv')
# customer = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/projects/cognixia/data/customer_data.csv')
# df = pd.merge(churn, customer, on='customerID')

# tel = pd.merge(df, internet, on='customerID')
# for col in ['PhoneService', 'PaperlessBilling', 'Churn', 'Partner', 'Dependents']:
#     tel[col] = tel[col].map({'Yes': 1, 'No': 0})

# vars = ['Contract', 'PaymentMethod', 'gender', 'InternetService']
# d = pd.get_dummies(tel[vars], drop_first=True)
# tel = pd.concat([tel, d], axis=1)

# tel.drop(vars, inplace=True, axis=1)

# t = []
# for col in tel.columns:
#     if tel[col].dtype == 'O':
#         print(col, '-->\t\t', tel[col].unique())
#         t.append(col)

# for col in t[3:]:
#     d = pd.get_dummies(tel[col], prefix=col)
#     d.drop(col+'_No internet service', axis=1, inplace=True)
#     tel = pd.concat([tel, d], axis=1)

# tel.drop(t[3:], axis=1, inplace=True)

# tel.drop('customerID', axis=1, inplace=True)

# tel['TotalCharges'] = pd.to_numeric(tel['TotalCharges'], errors='coerce')

# tel.dropna(inplace=True)
# d = pd.get_dummies(tel['MultipleLines'], prefix='MultipleLines')
# d.drop('MultipleLines_No phone service', axis=1, inplace=True)
# tel = pd.concat([tel, d], axis=1)
# tel.drop('MultipleLines', axis=1, inplace=True)

# X = tel.drop('Churn', axis=1)
# y = tel['Churn']


# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# # feature scaling -- standard scaler
# from sklearn.preprocessing import StandardScaler
# sc = StandardScaler()
# vars = ['tenure', 'MonthlyCharges', 'TotalCharges']
# X_train[vars] = sc.fit_transform(X_train[vars])
# X_test[vars] = sc.transform(X_test[vars])

# import statsmodels.api as sm
# logm1 = sm.GLM(y_train, sm.add_constant(X_train), family=sm.families.Binomial())
# res = logm1.fit()
# y_train_pred = res.predict(sm.add_constant(X_train))
# y_train_pred[:10]
# y_train_pred = y_train_pred.values.reshape(-1)
# y_train_pred[:10]
# print(res.summary())
# # print(X_train.columns[~rfe.support_ == False])
# logreg = LogisticRegression() 

# from sklearn.feature_selection import RFE 
# rfe = RFE(logreg, n_features_to_select=15) 
# rfe = rfe.fit(X_train, y_train)
# print(rfe.support_)
# list(zip(X_train.columns, rfe.support_, rfe.ranking_))
# X_train.columns[~rfe.support_]
# X_train.columns[rfe.support_ == False]
# cols = X_train.columns[rfe.support_]
# print(cols)

# import statsmodels.api as sm
# X_train_sm = sm.add_constant(X_train[cols])
# logm1 = sm.GLM(y_train, X_train_sm, family=sm.families.Binomial())
# res = logm1.fit()
# res.summary()
# # print(X_train_sm.)
# y_train_pred = res.predict(X_train_sm)
# print(y_train_pred[:5])
# y_train_pred = y_train_pred.values.reshape(-1)
# print(y_train_pred[:5])
# y_train_pred_final = pd.DataFrame({'Churn':y_train.values,'Churn_prob':y_train_pred})
# y_train_pred_final['CustID'] = y_train.index
# y_train_pred_final['predicted'] = y_train_pred_final.Churn_prob.map(lambda x: 1 if x>0.5 else 0)
# print(y_train_pred_final.head())
# print(accuracy_score(y_train_pred_final.Churn,y_train_pred_final.predicted))
# print(confusion_matrix(y_train_pred_final.Churn,y_train_pred_final.predicted))