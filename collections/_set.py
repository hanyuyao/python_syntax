'''
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
'''

# python sets are written with curly brackets
s = {'Allen', 'Ben', 'Cindy'}
for name in s:
    print(name, end=' ')
print()

# add one item
s.add('Lisa')
print(s)

# add several items
s.update(['Tony', 'Jeff', 7+5j])
print(s)
print(len(s))       # 7
print('----------------------------------------')

# remove item
# if the item doesn't exist, remove will raise an error, but discard won't
s.remove(7+5j)
s.discard('Jeff')
print(s)
print(s.pop())      # s.pop() returns the removed item, it removes different items in every execution

s.clear()
del s
print('----------------------------------------')

# join tow sets
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.union(s2))     # returns a new set
s1.update(s2)
print(s1)
print('----------------------------------------')

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1.difference(s2))
print(s1.intersection(s2))