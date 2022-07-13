import pandas as pd

df = pd.read_csv('iris.csv')

print("\n", df.head())

print("\n", df.head().isnull())

print("\n", df.isnull().sum())
print("\n", df.duplicated())

