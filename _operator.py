# arithmetic operator
print("Arithmetic operator: ")
x, y = 13, 2
print(x/y)          # 6.5
print(x//y)         # 6
print(x**y)         # 13^2
print(pow(x, y))    # 13^2
print("------------------------------------------")


# assignment operator
'''
=
-=
+=
*=
/=
//=
%=
**=
&=
|=
^=
>>=
<<=
'''

# logical operator
print("Logical operator: ")
print( 18 > 4 and 8 < 10 )
print( 18 > 4 or 3 != 3 )
print(not 8<9 and 9<3)     # False, indicating that "not" perform first then "and"
print("------------------------------------------")


# identity operator
'''
Identity operators are used to compare the objects, 
not if they are equal, but if they are actually the same object, 
with the same memory location
'''
print("Identity operator: ")
x, y, z = 1, 2, 1
print(x is not y)   # True
print(x is z)       # True
print("------------------------------------------")


# membership operator
print("Membership operator: ")
x = ['a', 'b', 'c']
print('a' not in x)     # False
y = (1, 2, 3)
print(4 in y)           # False
z = {"Allen":21, "Ben":18, "Kiddy":49}
print("Ben" in z)       # True


# bitwise operator
'''
&
|
^
~
<<
>>
^ is the most important bitwise operator, when solving problems associate with numbers, think of ^
Ex: “Given a set of numbers where all elements occur even number of times 
except one number, find the odd occurring number” -> doing XOR of all numbers
'''
