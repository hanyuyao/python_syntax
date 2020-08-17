import numpy as np

# access 2-D array
arr = np.array([[1,2,3], [4,5,6]])
print(arr[1, 2])        # 6

# access 3-D array
arr = np.array([[[1,2,3],[4,5,6]],
                [[7,8,9],[10,11,12]]])
print(arr[1, 0, 1])     # 8

# 1-D ndarray slicing
'''
[start:end]         
[start:end:step]
***'end' is not included!!!***
negative step: reverse picking

1. [::2] -> start from the beginning to the end, pick an element in every two elements
2. [::-1] -> reverse the ndarray
3. [2::-1] -> strat from index 2 and reversely pick elements
'''

# 2-D ndarray slicing
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[:,:], '\n')
print(arr[:,2], '\n')
print(arr[0:2, 1:3], '\n')
print(arr[::-1, ::-1], '\n')        # reverse both dimension
print(arr[1::-1, ::-1], '\n')
print(arr[2:0:-1, ::-1], '\n')