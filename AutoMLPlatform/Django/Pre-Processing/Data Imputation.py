# -*- coding: utf-8 -*-
"""Data Imputation

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14VOEsPTE0JsjP0upUsdz3OSq1BzubNbk
"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#read data from given xls
from google.colab import drive
drive.mount('/gdrive')
# %cd /gdrive
!ls
# %cd MyDrive
data = pd.read_excel('data.xls')
data
#look the first 5 records of data
data.head(5)
# check column names, not null count and data types 
print("\n-------------------Checked Column Names-------------------\n")
for col in data.columns: 
    print(col)
print("\n------------------------Not Null Count---------------------\n")
print(data.isna())
print("\n------------------------Summary---------------------\n")
print(data.isna().sum())
print("\n------------------------Data Types------------------------\n")
print(data.info())
print(dropna(thresh=2))
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
print(X)