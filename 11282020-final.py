print("10282020-final")
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

movies = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/projects/cognixia/data/movies.csv')
print(movies.head())
ratings = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/projects/cognixia/data/ratings.csv')
print(ratings.head())
print(movies.info())
print(ratings.info())
print(len(movies))
print(len(ratings))
df = pd.merge(ratings,movies,on='movieId')
df.groupby('title')['rating'].mean().sort_values(ascending=False)
print(df.head())
print(df.groupby('title')['rating'].count().sort_values(ascending=False).head(10))
rating = pd.DataFrame(df.groupby('title')['rating'].mean())
print(rating.head(20))
rating['number_of_ratings'] = df.groupby('title')['rating'].count()
print(rating.head(10))
# print(df.head())
# print(list(df.groupby('title'))[:2])
sns.jointplot(x='rating',y='number_of_ratings',data=rating)
# plt.show()
rating_mat=df.pivot_table(values='rating',index='userId',columns='title')
print(rating_mat.head())
print(movies.title.head(10))
movies[movies.title =='Forrest Gump (1994)']
fg = rating_mat['Forrest Gump (1994)']
similar_to_fg = rating_mat.corrwith(fg)
corr_fg = pd.DataFrame(similar_to_fg, columns=['correlation'])
corr_fg.dropna(inplace=True)
# print(corr_fg.head())
corr_fg = corr_fg.join(rating.number_of_ratings)
print(corr_fg.head())

rating_mat=df.pivot_table(values='rating',index='userId',columns='title')
movies[movies.title =='Matrix, The (1999)']
mat = rating_mat['Matrix, The (1999)']
similar_to_mat = rating_mat.corrwith(mat)
corr_mat = pd.DataFrame(similar_to_mat, columns=['correlation'])
corr_mat.dropna(inplace=True)
# print(corr_mat.head())
corr_mat = corr_mat.join(rating.number_of_ratings)
print(corr_mat.head())
print(corr_fg[corr_fg['number_of_ratings']>40].sort_values('correlation',ascending=False).head(15))
# a = np.array([2,3,4,10,11,12,20,25,30])
# # df = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/projects/cognixia/data/AdultIncome.csv')
# # print(df.head())
# k = 2
# c1 = 4
# c2 = 12
# k1 = {2,3,4}
# k2 = {10,11,12,20,25,30}
# c3 = 3 # average of k1
# c4 = 18 #average of k2
# k3 = {2,3,4,10}
# k4 = {11,12,20,25,30}
# c5 = 4.75
# c6 = 19.6
# k5 = {2,3,4,10,11,12}
# k6 = {20,25,30}
# c7 =7
# c8 = 25
# k7 = {2,3,4,10,11,12}
# k8 = {20,25,30}
# print(k7)
# print(k8)
# x = np.array([1,5,1.5,8,1,9])
# y = np.array([2,8,1.8,8,0.8,11])
# # print(sns.scatterplot(x,y))
# # sns.scatterplot(x,y) 
# # plt.show()
# from sklearn.cluster import KMeans
# km = KMeans(n_clusters=2)
# X = np.array([[1,2],[5,8],[1.5,1.8],[8,8],[1,0.8],[9,11]])
# km.fit(X)
# print(km.cluster_centers_)
# # sns.scatterplot(x,y,color='blue')
# # sns.scatterplot(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='red',marker='*',s=200)
# # plt.show()

# df = pd.read_excel('/Users/stomar-n/001_sudhir_2020_nmac/projects/cognixia/data/Cluster_Problem_Dataset.xlsx')
# print(df.head())
# print(len(df))
# print(df.info())
# print(df.dropna(inplace=True))
# print(df)

# X = df.iloc[:,:2].values
# print(X[:2])

# from sklearn.preprocessing import StandardScaler
# sc = StandardScaler()
# X = sc.fit_transform(X)
# print(X[:2])
# pd.DataFrame(X,columns=['CO2','GDP'])
# df = pd.concat([df,pd.DataFrame(X,columns=['CO2','GDP'])],axis=1)
# print(df.head())

# X = pd.DataFrame(X,columns=['CO2','GDP'])
# print(X.head())

# lst = []
# for i in range(1,11):
#     km = KMeans(n_clusters=i,random_state=0)
#     km.fit(X)
#     lst.append(km.inertia_)
# print(lst)
# # plt.plot(range(1,11),lst,marker='o')
# # plt.show()

# k=3
# from sklearn.cluster import AgglomerativeClustering
# from scipy.cluster.hierarchy import dendrogram, linkage
# df = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/projects/cognixia/data/Mall_Customers.csv')
# # import sklearn
# # print(dir(sklearn))
# print(df.head())
# print(df.info())
# X = df.iloc[:,[3,4]].values
# print(X[:5])

# # lst = []
# # for i in range(1,11):
# #     km = KMeans(n_clusters=i,random_state=0)
# #     km.fit(X)
# #     lst.append(km.inertia_)
# # print(lst)
# # plt.plot(range(1,11),lst,marker='o')
# # plt.show()

# # plt.figure(figize=(15,10))
# den = dendrogram(linkage(X,method='ward'))
# # plt.show()
# hc = AgglomerativeClustering(n_clusters=5)

# print(hc.fit_predict(X))


# from sklearn.datasets import load_iris
# iris = load_iris()
# df = pd.DataFrame(iris.data, columns = iris.feature_names)
# print(df.head())
# df['cluster'] = iris.target
# print(df.head())


# #KNN - K Nearest Neighbours
# df = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/projects/cognixia/data/diabetes.csv')
# print(df.head())
# print(len(df))
# df.Outcome.unique()
# c=df.corr()
# print(c['Outcome'])
# sns.heatmap(df.corr(),annot=True,cmap='coolwarm')
# # plt.show()
# # array([1,0])
# from sklearn.model_selection import train_test_split
# X = df.iloc[:,:-1].values
# Y = df.iloc[:,-1].values
# print(X)
# print(Y)
# X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=123)
# print(X_train)
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import accuracy_score,confusion_matrix
# knn = KNeighborsClassifier(n_neighbors=50)
# knn.fit(X_train,Y_train)
# Y_pred=knn.predict(X_test)
# print(accuracy_score(Y_test,Y_pred))
# # print()