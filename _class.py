'''
The 'self' parameter is a reference to the current instance (object which is created from a class) 
of the class, and is used to access variables that belong to the class.
'self' has to be the first parameter of any function in the class.
'''

class Point:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
    
    def show(self):
        print('(', self.x, ',', self.y, ')')

p = Point(2.5, 3.7)
p.show()

# delete the y property from the p object
del p.y

# delete object p
del p


'''
Inheritance:
The child's __init__() function overrides the inheritance of the parent's __init__() function.
If child class has a method that has the same name as parent class method, it will overrides the parent class method
'''
class Point3D(Point):
    def __init__(self, x:float, y:float, z:float):
        super().__init__(x, y)
        self.z = z
    
    def show3d(self):
        print("( {}, {}, {} )".format(self.x, self.y, self.z))

p2 = Point3D(1, 2, 3)
p2.show()
p2.show3d()