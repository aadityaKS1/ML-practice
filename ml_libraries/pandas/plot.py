import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('data.csv')
# df.plot()
# plt.show()
# for scatter plot
# df.plot(kind='scatter',x='Duration',y='Maxpulse')#for two column 
# plt.show()

#histogram (one column only)
df['Duration'].plot(kind='hist')
plt.show()