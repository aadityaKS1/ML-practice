import pandas as pd

df=pd.read_csv('cleandata.csv')
df['Date']=pd.to_datetime(df['Date'],format='mixed')

print(df.to_string())
df.dropna(subset=['Date'],inplace=True)#remove the row 22 since date is empty
print(df.to_string())

#replace 450 with row 7 iwth 45
# df.loc[7,'Duration']=45
# print(df.to_string())

#using loop for larger data
# for x in df.index:
#     if df.loc[x,"Duration"]>120:
#         df.loc[x,"Duration"]=120
# print(df.to_string())

#remove row wtihwrong data
for x in df.index:
    if df.loc[x,"Duration"]>120:
        df.drop(x,inplace=True)
print(df.to_string())
# print(df.duplicated())
df.drop_duplicates(inplace=True)
print(df.to_string())