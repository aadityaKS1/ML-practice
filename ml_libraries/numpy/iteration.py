import numpy as np

arr=np.array([1,2,3,4,5])
for x in arr:
    print(x)
arr2d=np.array([[1,2,3,4,5],[6,7,8,9,10]])
for x in arr2d:
    for y in x:
        print(y)
arr3d=np.array([[[1,2,3,4],[5,6,7,8]],
               [[9,10,11,12],[13,14,15,16]]])
# for x in arr3d:
#     for y in x:
#         for z in y:
#             print(z)
#using nditer()
for  x in np.nditer(arr3d):
    print(x)
#iterating Array with diffent datay types
for x in np.nditer(arr,flags=['buffered'],op_dtypes=['S']):
    print(x)
#ITERAING with different shapesize
for x in np.nditer(arr3d[:,:,::2]):
    print(x)
#Enumerate the following array
for idx,x in np.ndenumerate(arr):
    print(idx,x)
for idx,x in np.ndenumerate(arr2d):
    print(idx,x)