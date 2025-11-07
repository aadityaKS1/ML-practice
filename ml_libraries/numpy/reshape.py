import numpy as np

arr=np.array([1,2,3,4,5,6,7,8])
newarr=arr.reshape(4,2)#four row  2 elements each
print(newarr)
arr2=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr2=arr2.reshape(2,3,2)
#newarr2=arr2.reshape(2,3,-1) #this is also valid can avoid calcualtion of one diemaniosn 
print(newarr2)
# check if the returnded array is copy or view
print(arr.reshape(4,2).base)
print(arr2.reshape(2,3,2).base)
#multidimenion to 1
arr2d=np.array([[1,2,3,4],[5,6,7,8]])
newarr3=arr2d.reshape(-1)
print(newarr3)
