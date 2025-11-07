import pandas as pd

# Working with Json


df=pd.read_json('train.json')

df.dtypes
#df=pd.read_json("url")
 # Working with SQl  
 !pip install mysql.connector
import mysql.connector

conn=mysql.connector.connect(host='localhost',user='root',password='',database='world')
pd.read_sql_query("SELECT * FROM city",conn)
pd.read_sql_query("SELECT * FROM city WHERE CountryCode LIKE 'IND'",conn)
pd.read_sql_query("SELECT * FROM country WHERE LifeExpectancy  >30",conn)
pd.read_sql_query("SELECT * FROM countrylanguage",conn)
