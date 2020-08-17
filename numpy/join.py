import numpy as np

# 1D array concatenation
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
arr = np.concatenate((arr1, arr2))
print(arr.base)         # None, it a copy
print(arr)
print('------------------------------------\n')

# 2D array concatenation
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(np.concatenate((arr1, arr2), axis=0), '\n')
print(np.concatenate((arr1, arr2), axis=1))
print('------------------------------------\n')

# 3D array concatenation
arr1 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
arr2 = np.array([[[1, 1], [0, 0]], [[1, 1], [0, 0]]])
arr = np.concatenate((arr1, arr2), axis=1)          # try axis=0, 1, 2
print(arr.shape, '\n', 'dimension:', arr.ndim)
print(arr)
print('------------------------------------\n')

# stacking
# https://www.w3schools.com/python/numpy_array_join.asp