import random

# this is a comment
"""
this is a multiline string 
it is also a comment
"""

if __name__ == "__main__":
    print("1. variable type")
    x, y = 2, 3.2
    print(type(x), type(y))
    x, y = y, x
    print(type(x), type(y))
    x = complex(8+3j)
    x = float(5.62)
    x = int(5)
    x = str(x)
    print()

    print("2. random number")
    print("Random number:", random.randrange(1, 100))
    print()

    print("3. boolean")
    # True
    print(bool("allen"))
    print(bool(['a', 'b', 'c']))
    # False
    print(bool(""))     # empty string
    print(bool([]))     # empty list
    print(bool({}))     # empty dictionary
    print(bool(()))     # empty tuple
    print()

    print("4. while...else..., for...else...")
    i = 3
    while i > 0:
        print(i, end=' ')
        i -= 1
    else:
        print()     # print a new line once the condition is false
    
    for x in range(3):
        print(x, end=' ')
    else:
        print()     # print a new line once the condition is false


