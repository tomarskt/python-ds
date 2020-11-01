print("Hello - 10302020")
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
gas = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/cognexia_training_python/10232020/Data/gas_prices.csv')
print(gas.head(2))
plt.figure(figsize=(12,7)) 
plt.plot(gas['Year'], gas['Canada'], 'bo-.', markersize=8, markerfacecolor='green', markeredgecolor='red') 
plt.plot(gas['Year'], gas['France'], 'bo-.', markersize=8, markerfacecolor='green', markeredgecolor='red') 
plt.title('Gas price for Canada') 
plt.xlabel('Year') 
plt.ylabel('Gas price in USD') 
plt.savefig('/Users/stomar-n/001_sudhir_2020_nmac/cognexia_training_python/10232020/gas.png') 
plt.show()

print(gas.columns)
plt.figure(figsize=(12,7))
for c in gas.columns[1:]:
    plt.plot(gas['Year'],gas[c])
plt.legend(gas.columns[1:])
plt.show()

# scatter
# pie, 
# box & wisker
# # heatmap

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
import warnings 
warnings.filterwarnings('ignore')
# df = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/cognexia_training_python/10232020/Data/NSE-INFY.csv') 
# df.head()
# plt.plot(df.Close) 
# plt.plot(df['Close']) 
# plt.plot(df.Last)
sns.barplot(['A', 'B', 'C'], [233, 120, 200])
sal = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/cognexia_training_python/10232020/Data/Salary_Data.csv') 
sal.head()
sns.scatterplot(sal.YearsExperience, sal.Salary) 
plt.show()


# x = np.random.rand(50)
# y = np.random.rand(50)
# colors = np.random.rand(50)
# area = (15 * np.random.rand(50)) ** 2
# sns.scatterplot(x,y,s=area,c=colors)

x=np.random.rand(50) 
y=np.random.rand(50) 
colors=np.random.rand(50) 
area=(10*np.random.rand(50)) ** 2 
print(area) 
plt.scatter(x,y, s=area, c=colors) 
plt.show()

engineers = (244,540,324,300,150)
cities = ['New Delhi', 'Mumbai','Tokyo','Montreal','Bangalore']
plt.pie(engineers,labels=cities,startangle=90,autopct='%0.2f%%')
plt.show()

engineers = (244,540,324,300,150)
cities = ['New Delhi', 'Mumbai','Tokyo','Montreal','Bangalore']
plt.pie(engineers,labels=cities,startangle=90,autopct='%0.2f%%',explode=[0,0,0,0.2,0])
plt.show()

titanic = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/cognexia_training_python/10232020/Data/titanic.csv')

titanic.head()

sns.countplot(x='Sex',data=titanic,hue='Survived')

x=np.linspace(0,5,11)
plt.subplot(2,3,1)
plt.plot(x,x**2,'--')
plt.plot(x,x*2,'--')
plt.subplot(2,2,2)
sns.countplot(x='Sex',data=titanic,hue='Survived')
plt.subplot(2,3,4)
sns.boxplot(x=titanic.Fare)

df = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/cognexia_training_python/10232020/Data/ml-dataset-breast-cancer.csv')
df.head()

df.diagnosis.unique()

df.shape

df['Unnamed: 32'].unique()

df.drop(['id','Unnamed: 32'], axis=1, inplace=True)

plt.figure(figsize=(15,10))
sns.heatmap(df.corr(),cmap='viridis',annot=True)

plt.figure(figsize=(15,10))
sns.heatmap(df.corr(),cmap='viridis',annot=True)


tips=sns.load_dataset('tips')
tips.head()
tips.describe)