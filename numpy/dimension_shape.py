import numpy as np

print(np.__version__)
arr = np.array((1, 2, 3, 4, 5))     # list, tuple or any array-like object to create ndarray object
print(arr)
print(type(arr))
print(arr.shape)
print("-------------------------------------\n")

print("0-D array: ")    # arr.ndim = 0
print(np.array(35), '\n')

print("1-D array:")     # arr.ndim = 1
print(np.array([1, 2, 3, 4, 5]), '\n')

print("2-D array:")
print(np.array([[1, 2, 3], [4, 5, 6]]), '\n')

print("3-D array:")     # arr.ndim = 2
arr = np.array([[[1,2,3],[4,5,6]],
                [[7,8,9],[1,2,3]]])
print(arr)
print('array.shape:', arr.shape)
print('array.ndim:', arr.ndim)
print("-------------------------------------\n")

print("5-D array:")
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('array.shape:', arr.shape)
print('array.ndim:', arr.ndim, '\n')
print("-------------------------------------\n")

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# -1 represent unknown dimension, numpy will calculate this number
newarr = arr.reshape((2, 3, -1))
print(newarr)
print(newarr.base)          # [ 1  2  3  4  5  6  7  8  9 10 11 12], it's a view
print("-------------------------------------\n")

# flatten the array
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1).copy()
print(newarr)
print(newarr.base)          # None, it's a copy
