import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# use np.nditer() to iterate numpy array
for x in np.nditer(arr):
    print(x, end=' ')  
print()

# iterating numpy array with different data type
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x, end=' ')
print()

# iterating with different step size
for x in np.nditer(arr[:, 1, ::2]):
    print(x, end=' ')
print('\n----------------------------------------------\n')

# enumerated iteration using udenumerate()
# type(idx) : tuple
for idx, x in np.ndenumerate(arr):
    print(idx, x)