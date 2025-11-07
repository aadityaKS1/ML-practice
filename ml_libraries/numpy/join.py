import numpy as np

arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])
arr=np.concatenate((arr1,arr2))
print(arr)
arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])
arr=np.stack((arr1,arr2),axis=1)#convert in 2d array crating collumns one form each elemtn
print(arr)
arr=np.hstack((arr1,arr2))#stacking along rows
print(arr)
arr=np.vstack((arr1,arr2))#along column 
print(arr)
arr=np.dstack((arr1,arr2))#stacking along depth also convert in to 3d
print(arr)
arr21=np.array([[1,2,3,4],[5,6,7,8]])
arr22=np.array([[11,12,13,14],[15,16,17,18]])
arr2d=np.concatenate((arr21,arr22),axis=1)#axis 1 for combining two rowws in to 1
print(arr2d)
