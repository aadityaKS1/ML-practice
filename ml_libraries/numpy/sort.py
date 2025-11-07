import numpy as np

arr=np.array([1,2,3,5,76,75,6,4,5,7])
print(np.sort(arr)) #returns copy of the array
arr2 = np.array(['banana', 'cherry', 'apple'])#alphatbetical order
print(np.sort(arr2))
arr3 = np.array([True, False, True])#alphabetical order
print(np.sort(arr3))
arr4= np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr4))#sorted in each array 