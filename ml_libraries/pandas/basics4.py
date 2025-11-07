import pandas as pd

df=pd.read_csv('data.csv')
print(df.head(10))#print first 10 rows
print(df.head())#print first 5 rows
print(df.tail())#print last 5 rows
print(df.tail(20))#print last 20 rows
print(df.info())
