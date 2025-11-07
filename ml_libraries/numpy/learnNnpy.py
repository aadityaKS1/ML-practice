import numpy as np

arr=np.array([1,2,3,4,5,6,7,8])#one dimension
arr2=np.array((1,2,3,4,5,4))
print(arr)
arr0d=np.array(22)# 0-dimension
print(arr2)
print(arr0d)
print(type(arr))
print(np.__version__)
# 2 dimension array
arr2d=np.array([[1,2,3,34,66,77],
               [32,55,33,4,88,99],
               [2,3,4,67,61,39]])
print(arr2d)
# 3 dimension array
arr3d=np.array([[[11,32,53],[32,55,33]],[[1,2,3],[32,1,3]]])
print(arr3d)
print(arr.ndim)
print(arr0d.ndim)
print(arr2d.ndim)
print(arr3d.ndim)

arrhd=np.array([2,3,4,5,6],ndmin=5)
print(arrhd)
#access 2d array
print("2nd element on first row:",arr2d[0,1])
print("3rd element on 2nd row:",arr2d[1,2])
#access 3d array
print("2nd element on first row in first array:",arr3d[0,0,1])
print("3rd element on 2nd row in 2nd array:",arr3d[1,1,2])
#negative indexing
print("Last element form 2nd dim:",arr2d[1,-1])
#slicing
print(arr[1:3])
print(arr[4:])
print(arr[:4])
#negative slicing
print(arr[-3:-1])# this also doesnot include value at last indx
#using step
print(arr[::2])
#2d slicing 
print(arr2d[1,1:3])
print(arr2d[0:3,2])#return element fo second index form each array
print(arr2d[0:3,2])#return element of range sliced form each array
