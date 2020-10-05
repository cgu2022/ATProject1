import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('data.csv', header = 0)
df = df.drop(['id'], axis=1)
print(df.head())
print('Description =')
print(df.describe())
print('Info =')
print(df.info())