import numpy as np

''' numpy data type
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
'''

# check the data type of an adarray object
arr = np.array([1, 2, 3, 'allen'])
print(arr.dtype)

arr = np.array(['ben', 'Allen'])
print(arr.dtype)

arr = np.array([1, 2, 3, 4])
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='i8')        # 8 bytes integer
print(arr.dtype)
print("-------------------------------------------")

arr = np.array([1.2, 2.5, 3.7])
print(arr.dtype)
newarr = arr.astype(int)        # == arr.astype('i')
print(newarr)
print(newarr.dtype)
print("-------------------------------------------")

arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)