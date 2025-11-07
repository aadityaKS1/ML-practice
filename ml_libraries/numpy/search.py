import numpy as np

arr=np.array([1,2,3,5,76,75,6,4,5,7])
x=np.where(arr==5)
print(x)
y=np.where(arr%2==0)
print(y)
z=np.where(arr%2==1)
print(z)
#where shouldbe the value inserted to  maintain search order
x=np.searchsorted(arr,[2,4,6])
print(x)
#search from the right side
m=np.searchsorted(arr,2,side='right')
print(m)