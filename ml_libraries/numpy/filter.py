import numpy as np

arr1=np.array([1,2,3,4,5])
x=np.array([True,False,False,True,True])
newarr=arr1[x]
print(newarr)
arr2=np.array([345,565,322,555])
filter_arr=[]
for x in arr2:
    if x>400:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr2=arr2[filter_arr]
print(filter_arr)
print(newarr2)
#or
arr = np.array([41, 42, 43, 44])
filter_arr2=arr>42
newarr3=arr[filter_arr2]
print(newarr3)
