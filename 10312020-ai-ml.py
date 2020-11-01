print("hello-10312020")
import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
df = pd.read_csv('/Users/stomar-n/001_sudhir_2020_nmac/cognexia_training_python/10232020/Data/Salary_Data.csv')
print(df.head())
# y = mc + c
# sal = m*exp + c
sns.scatterplot(df.Salary,df.YearsExperience)
plt.show()