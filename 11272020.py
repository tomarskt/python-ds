print("10272020-k means clustering")
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

a = np.array([2,3,4,10,11,12,20,25,30])
# df = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/projects/cognixia/data/AdultIncome.csv')
# print(df.head())
k = 2
c1 = 4
c2 = 12
k1 = {2,3,4}
k2 = {10,11,12,20,25,30}
c3 = 3 # average of k1
c4 = 18 #average of k2
k3 = {2,3,4,10}
k4 = {11,12,20,25,30}
c5 = 4.75
c6 = 19.6
k5 = {2,3,4,10,11,12}
k6 = {20,25,30}
c7 =7
c8 = 25
k7 = {2,3,4,10,11,12}
k8 = {20,25,30}
print(k7)
print(k8)
x = np.array([1,5,1.5,8,1,9])
y = np.array([2,8,1.8,8,0.8,11])
# print(sns.scatterplot(x,y))
# sns.scatterplot(x,y) 
# plt.show()
from sklearn.cluster import KMeans
km = KMeans(n_clusters=2)
X = np.array([[1,2],[5,8],[1.5,1.8],[8,8],[1,0.8],[9,11]])
km.fit(X)
print(km.cluster_centers_)
# sns.scatterplot(x,y,color='blue')
# sns.scatterplot(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='red',marker='*',s=200)
# plt.show()

df = pd.read_excel('/Users/stomar-n/001_sudhir_2020_nmac/projects/cognixia/data/Cluster_Problem_Dataset.xlsx')
print(df.head())
print(len(df))
print(df.info())
print(df.dropna(inplace=True))
print(df)

X = df.iloc[:,:2].values
print(X[:2])

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)
print(X[:2])
pd.DataFrame(X,columns=['CO2','GDP'])
df = pd.concat([df,pd.DataFrame(X,columns=['CO2','GDP'])],axis=1)
print(df.head())

X = pd.DataFrame(X,columns=['CO2','GDP'])
print(X.head())

lst = []
for i in range(1,11):
    km = KMeans(n_clusters=i,random_state=0)
    km.fit(X)
    lst.append(km.inertia_)
print(lst)
# plt.plot(range(1,11),lst,marker='o')
# plt.show()

k=3
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
df = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/projects/cognixia/data/Mall_Customers.csv')
# import sklearn
# print(dir(sklearn))
print(df.head())
print(df.info())
X = df.iloc[:,[3,4]].values
print(X[:5])

# lst = []
# for i in range(1,11):
#     km = KMeans(n_clusters=i,random_state=0)
#     km.fit(X)
#     lst.append(km.inertia_)
# print(lst)
# plt.plot(range(1,11),lst,marker='o')
# plt.show()

# plt.figure(figize=(15,10))
den = dendrogram(linkage(X,method='ward'))
# plt.show()
hc = AgglomerativeClustering(n_clusters=5)

print(hc.fit_predict(X))


from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns = iris.feature_names)
print(df.head())
df['cluster'] = iris.target
print(df.head())


#KNN - K Nearest Neighbours