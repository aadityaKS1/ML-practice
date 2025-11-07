import pandas as pd

data={
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df=pd.DataFrame(data)
print(df.loc[0])
print(df.loc[[0,1]])

a=[2,3,4]
myvar2=pd.Series(a,index=["x","y","z"])
print(myvar2.loc["x"])# return value at x index

#load csv file to daataframe
df1=pd.read_csv('data.csv')
print(df1)