import pandas as pd
import numpy as np
# s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)
# dates = pd.date_range('20130101', periods=6)
# df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
# print(df)
import matplotlib.pyplot as plt
# img = plt.imread('/Users/stomar-n/001_sudhir_2020_nmac/cognexia_training_python/flower.jpeg')
# plt.imshow(img)
# plt.show()
# img2=img[20:300,10:300]
# plt.imshow(img2)
# plt.show()
a = np.arange(26)
mylist = list('abcdefghijklmnopqrstuvwxyz')
print(mylist)
print(len(mylist))
mydict = dict(zip(mylist,a))
print(mydict)
s = pd.Series(mydict)
print(s)
print(s.values)
print(s.shape)
print(s.index)

mylist = [2,4,6,8]
s2 = pd.Series(mylist)
print(s2)
print(s2.index)
data = {'day':[1,2,3,4,5],'visitors':[344,450,300,390,342],'bounce_rate':[20,18,27,30,12]}
print(type(data))
df = pd.DataFrame(data)
print(df)
print(df.visitors)
print(df['visitors'])
print(df.shape)
print(df.index)
print(df.columns)
print(df.info)
print(df[df['visitors']>300])

d = {'A': [1,2,np.nan], 'B': [4,np.nan,np.nan], 'C': [7,8,9]}
df = pd.DataFrame(d)
print(df)
titanic = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/cognexia_training_python/10232020/Data/titanic.csv')
print(titanic.head)
print(len(titanic))
print(len(titanic.columns))
print(titanic.info)
# print(len(titanic.Name))
# d={'Day':[1,2,3,4,5,6,7], 'Visitors':[300,400,230,230,400,600,450],'Bounce_rate':[100,50,20,40,10,30,70]} 
# pd.DataFrame(d)
# print(pd.DataFrame(d))