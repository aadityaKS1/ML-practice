import pandas as pd

mydataset={
    'cars' :["BMW","Volvo","Ford"],#all arrays must be of samelength
    'passings':[3,2,7]
}

myvar=pd.DataFrame(mydataset)
print(myvar)

#pandas version
print(pd.__version__)

#sries
a=[3,4,5]
myvar=pd.Series(a)
print(myvar)
print(myvar[0])#label
myvar2=pd.Series(a,index=["x","y","z"])
print(myvar2["y"])
print(myvar2["x"])
#key value concept in Series 

calories={"day1":420,"day2":390,"day3":500}
myvar3=pd.Series(calories)
print(myvar3)
print(myvar3["day2"])#also work as label
print(pd.Series(calories,index=["day1","day3"]))#fetching some values