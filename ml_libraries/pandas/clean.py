import pandas as pd

df=pd.read_csv('cleandata.csv')
#for removing empty values NaN
# df.dropna(inplace=True)
# print(df.to_string())

#for  replacing NULL values with number 130
# df.fillna(130,inplace=True)
# print(df.to_string())

#replace NUll Values  in the calorews column iwth number 130
# df.fillna({"Calories":130},inplace=True)
# print(df.to_string())

#rplace using mean 

# x=df["Calories"].mean()
# df.fillna({"Calories":x},inplace=True)
# print(df.to_string())

#replace using meadian 
# x=df["Calories"].median()
# df.fillna({"Calories":x},inplace=True)
# print(df.to_string)
# print(x)

#replace using mode
x=df["Calories"].mode()[0]
df.fillna({"Calories":x},inplace=True)
print(df.to_string)
print(x)