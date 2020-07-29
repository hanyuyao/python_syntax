'''
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
'''

# python list are written with square brackets

lst = [1, 2, 'allen', 'ben', 5.3, 8-5j]
print( type(lst[-5:-2]) )       # <class 'list'>
print( lst[-5:-2] )             # [2, 'allen', 'ben']
print(lst[:])                   # print(lst)
print('--------------------------------------------')

# loop through a list
for x in lst:
    print(x, end=' ')
print()

print( bool(2 in lst) )         # True
print( 'allen' not in lst )     # False
print( len(lst) )               # 6
print('--------------------------------------------')

# add item
lst.append('A')
lst.insert(3, 5+2j)         # insert an item at the specified index
print(lst)

# remove item, use "try...except..."" to handle error
# remove item, pop index
lst.remove(5+2j)
lst.pop()                   # pop last items 
lst.pop(0)                  # remove specified index
del lst[0]
print(lst)

lst.clear()
print(lst)
del lst
try:
    print(lst)              # name 'lst' is not defined
except:
    print('name \'lst\' is not defined')
print('--------------------------------------------')

# copy a list
# lst_1 = lst is wrong
lst = [1, 2, 3, 4, 5]
lst_1 = list(lst)           # = lst.copy()
lst.pop()
print(lst_1)

lst_1 = [1,2,3]
lst_2 = [4,5,6]
lst_3 = []
lst_3.append(lst_1)
lst_3.append(lst_2)
print(lst_3)        # [[1, 2, 3], [4, 5, 6]]
lst_2.remove(5)
print((lst_3))      # [[1, 2, 3], [4, 6]]
# need to use lst_3.append(list(lst_1))
print('--------------------------------------------')

# join 2 lists
lst_1 = [1,2,3]
lst_2 = ['a','b','c']
print(lst_1 + lst_2)

lst_1.extend(lst_2)
print(lst_1)
print(lst_2)
print('--------------------------------------------')

lst = [1, 1, 2, 3]
print(lst.count(1))         # 2
lst.reverse()               # compare c++ : std::reverse(vec.begin(),vec.end());
print(lst)
lst.sort()                  # compare c++ : std::sort(vec.begin(),vec.end());
print(lst)

# sort a list
lst = ['allen', 'ben', 'kiddy', 'tony']
def comp(x):
    return len(x)

lst.sort(reverse=True, key=comp)
print(lst)