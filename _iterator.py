'''
In python, an iterator is an object which implements the iterator protocol, 
which consist of the methods __iter__() and __next__().
'''

lst = ['a', 'b', 'c']
lstit = iter(lst)

for i in range(len(lst)):
    print(next(lstit), end=' ')
else: print()

# The for loop actually creates an iterator object and executes the next() method for each loop.
string = 'allen'
for x in string:
    print(x, end=' ')
else: print()
