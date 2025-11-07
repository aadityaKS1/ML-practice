import numpy as np
arr=np.array([1,2,3,4,5] ,ndmin=4)
x=arr.copy()
arr[0]=42
print(arr)
print(x)

#change in view make change in original and vice versa
y=arr.view()
arr[0]=42
print(y)
y[0]=88
print(y)
print(arr)
print(arr.shape)