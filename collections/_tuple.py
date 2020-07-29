'''
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
'''

# python tuples are written with round brackets

tup = (1, 2, 3, 'a', 'b')

# tuples are unchangable or immutable -> convert to list first
lst = list(tup)
lst.remove(3)
tup = tuple(lst)
print(tup)

# tuple with one item vs. list with one item
# one item tuple needa a comma
tup = ('allen',)
print(type(tup))        # <class 'tuple'>
lst = ['allen']
print(type(lst))        # <class 'list'>
tup = ('allen')
print(type(tup))        # <class 'str'>

tup = (5, 5, 8, 8, 6, 6, 5)
print(tup.count(5))     # 3

print(tup.index(8))     # 2 (return the first index whose item = 8)