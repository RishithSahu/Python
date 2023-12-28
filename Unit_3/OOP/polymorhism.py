# getter() and setter()
# getter() and setter() are used to get and set the values of instance variables.
# They are used to implement data hiding in Python.
# The getter() returns the value of the attribute.
# The setter() sets the value of the attribute.
# The property() function is used to define getter and setter methods.
# It returns a property object.

'''
    Polymorphism:
    Polymorphism means the ability to take multiple forms.
    Refers to the same function name (but different signatures) being uses for different types.
    
    Runtime Polymorphism:
    Runtime polymorphism or Dynamic Method Dispatch is a process in which a call to 
    an overridden method is resolved at runtime rather than compile-time.
    Python supports this through the method overriding and overloading

'''

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth

class Trianlge(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height

def calc_area(Shape):
    return Shape.area()

c = Circle(5)
r = Rectangle(10, 20)
t = Trianlge(10, 20)

print(calc_area(c))
print(calc_area(r))
print(calc_area(t))