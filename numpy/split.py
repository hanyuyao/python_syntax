import numpy as np

# array_split() worked properly, while split() would fail in some cases

# split 1D numpy array into three parts
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)
print(newarr[0], newarr[1], newarr[2])
print("--------------------------")

# split 2D numpy array into three parts
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
newarr = np.array_split(arr, 3)
print(newarr)
print(newarr[0], newarr[1], newarr[2])