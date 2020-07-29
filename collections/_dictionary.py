'''
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
'''

# python dictionary are written with curly brackets

dic = {
    'Allen':21,
    'Ben':18,
    'Kiddy':49
}

print(dic['Ben'])           # 18
print(dic.get('Kiddy'))     # 49

dic['Allen'] = 22
print(dic)
print('----------------------------------')

for x in dic:
    print(x, end=' ')       # x is the key
    print(dic[x])

for x in dic.values():
    print(x, end=' ')       # 22 18 49
print()
print('----------------------------------')

for x,y in dic.items():
    print(x + ": " + str(y))

print('Allen' in dic)       # True
print(len(dic))             # 3
print('----------------------------------')

dic['Logan'] = 20
dic.pop('Kiddy')
del dic['Ben']
print(dic) 
dic.clear()
del dic         # delete the whole dictionary
