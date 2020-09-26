import numpy as np

# https://thispointer.com/sorting-2d-numpy-array-by-column-or-row-in-python/

# sort by first column and then second column
lst = np.array([[3,6], [1,10], [3, 4]])
idx = np.lexsort(np.rot90(lst))
lst = lst[idx]
print(lst, '\n')

# sort by second column
idx = lst[:,1].argsort()
lst = lst[idx]
print(lst)