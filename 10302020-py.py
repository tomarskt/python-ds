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