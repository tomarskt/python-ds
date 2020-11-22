import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

import warnings
warnings.filterwarnings('ignore')
churn = pd.read_csv('/Volumes/MacData/Data/churn_data.csv')
customer = pd.read_csv('/Volumes/MacData/Data/customer_data.csv')
internet = pd.read_csv('/Volumes/MacData/Data/internet_data.csv')
df = pd.merge(churn, customer, on='customerID')

tel = pd.merge(df, internet, on='customerID')
for col in ['PhoneService', 'PaperlessBilling', 'Churn', 'Partner', 'Dependents']:
    tel[col] = tel[col].map({'Yes': 1, 'No': 0})

vars = ['Contract', 'PaymentMethod', 'gender', 'InternetService']
d = pd.get_dummies(tel[vars], drop_first=True)
tel = pd.concat([tel, d], axis=1)

tel.drop(vars, inplace=True, axis=1)

t = []
for col in tel.columns:
    if tel[col].dtype == 'O':
        print(col, '-->\t\t', tel[col].unique())
        t.append(col)

for col in t[3:]:
    d = pd.get_dummies(tel[col], prefix=col)
    d.drop(col+'_No internet service', axis=1, inplace=True)
    tel = pd.concat([tel, d], axis=1)

tel.drop(t[3:], axis=1, inplace=True)

tel.drop('customerID', axis=1, inplace=True)

tel['TotalCharges'] = pd.to_numeric(tel['TotalCharges'], errors='coerce')

tel.dropna(inplace=True)
d = pd.get_dummies(tel['MultipleLines'], prefix='MultipleLines')
d.drop('MultipleLines_No phone service', axis=1, inplace=True)
tel = pd.concat([tel, d], axis=1)
tel.drop('MultipleLines', axis=1, inplace=True)



X = tel.drop('Churn', axis=1)
y = tel['Churn']











X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# feature scaling -- standard scaler
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
vars = ['tenure', 'MonthlyCharges', 'TotalCharges']
X_train[vars] = sc.fit_transform(X_train[vars])
X_test[vars] = sc.transform(X_test[vars])

import statsmodels.api as sm
logm1 = sm.GLM(y_train, sm.add_constant(X_train), family=sm.families.Binomial())
res = logm1.fit()
res.summary()
y_train_pred = res.predict(sm.add_constant(X_train))
y_train_pred[:10]
y_train_pred = y_train_pred.values.reshape(-1)
y_train_pred[:10]


