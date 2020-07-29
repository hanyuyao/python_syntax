# Arbitrary Arguments, *args
# If the number of arguments is unknown, add a * before the parameter name
def func(*args):
    print(args[0])          # 25
    for x in args: print(x, end=' ')
    print()
func(25, 20, 18, 23)


# Keyword Arguments
def func_1(p1, p2, p3):
    print(p1, p2, p3, sep=', ')
func_1(p2='b', p3='c', p1='a')


# Arbitrary Keyword Arguments, **kwargs
def func_2(**kwargs):
    print(kwargs['allen'])
func_2(ben=18, kiddy=49, allen=21)


# The pass Statement
def func_3():
    pass


# Specify parameters' type and return type
def func_4(p1:int, p2:float, p3:complex) -> tuple:
    return (p1, p2, p3)
print(func_4(p2=2.5, p1=5, p3=2+6j))


# lambda function (only has one expression)
f = lambda x, y : x*y
print( f(3, 2) )            # 6


# use lambda function as anonymous function insida another function
def func_5(n:int):
    return lambda x : x*n

f1 = func_5(2)
f2 = func_5(3)

print(f1(10))       # 20
print(f2(10))       # 30