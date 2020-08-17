import numpy as np

'''
copy is a new array, view is just a view of the original array.
copy owns the data, and acts like an entire different array.
view does not own the data, view and original array changes together.
'''

arr = np.array([1, 2, 3, 4, 5], dtype='float')

x = arr.copy()
y = arr.view()

'''
base: numpy array attribute.
return None if the array owns the data.
otherwise, refers to the original object.
'''

print(arr.base)
print(x.base)
print(y.base)