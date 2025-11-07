import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9,10])
arr1=np.array_split(arr,5)# adjust automatic 
#arr1=np.split(arr,5) #use this if no remainder while dividing
# arr1=np.split(arr,4) this doesnot work
print(arr1)
for x in arr1:
    print(x)
#splitting 2d arrays
# arr2d=np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
# arr2=np.array_split(arr2d,3)
# print(arr2)
#splitting 2d arrays into column 
arr2d=np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
#arr2=np.array_split(arr2d,3,axis=1)#for 2d axis 1=column
arr2=np.hsplit(arr2d,2)
print(arr2)
arr2=np.vsplit(arr2d,3)
print(arr2)
