print("Hello - 10302020")
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
# df = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/cognexia_training_python/10232020/Data/tips.csv')
# df.head()
tips=sns.load_dataset('tips')
print(tips.head())
print(tips.describe())
print(tips.mean())
print(tips.total_bill.mean())
a=np.array([8,13,11,14,15,10,14,9,11,12,13])
print(a)
print(a.mean())

a=np.array([8,13,11,14,15,10,14,9,101,12,13,99,10])
print(a)
print(a.mean())

q1 = np.percentile(a,25)
q2 = np.percentile(a,50)
q3 = np.percentile(a,75)
print(q1)
print(q2)
print(q3)

from statistics import median, mode
print(median(a))
print(np.std(a))
a=np.array([4,5,8])
a=np.array([8,13,11,14,15,10,14,9,101,12,13,99,10])
mu = a.mean()
print(mu)
print(((4-mu)**2 + (5-mu)**2 + (8-mu)**2)/3)
print(np.sqrt(((4-mu)**2 + (5-mu)**2 + (8-mu)**2)/3))
print(np.std(a))
iqr = q3 - q1
lower_bound = q1 - 1.5*iqr
upper_bound = q3 + 1.5*iqr
print(iqr)
print(lower_bound)
print(upper_bound)
print(a)
print(a[(a<lower_bound) | (a>upper_bound)])
titanic = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/cognexia_training_python/10232020/Data/titanic.csv')
print(titanic.describe())
print(titanic[['Age','Fare']].describe())
print(titanic[['Age','Fare']].describe(percentiles=[0.05,0.10,0.15,0.20,0.5,0.7,0.8,0.9,0.95]))
# sns.boxplot(a)
# plt.show()
# sns.boxplot(titanic)
# plt.show()
sns.boxplot(tips.total_bill)
plt.show()

mu, sigma = 0.5, 0.1
s = np.random.normal(mu, sigma, 1000)
# Create the bins and histogram
count, bins, ignored = plt.hist(s, 20, normed=True)
# Plot the distribution curve
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
    np.exp( - (bins - mu)**2 / (2 * sigma**2) ),       linewidth=3, color='y')
plt.show()

# //z-score
