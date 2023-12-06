# Constructors(Initialise the obbjects) 
#             Automatically called special function __init__(self)

class add:
    def __init__(self,a,b):                 # Consturctor              
        self.a = a                          #     |              
        self.b = b                          # Consturctor
    def sum(self):
        return self.a + self.b
    
# sum = add(4,5)
# print(sum.sum())                  '''Calling class method'''

# Question 1: Create a class rectangle which has attributes length and breadth.
#             Also create a class method area and perimeter.

class rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        return self.l*self.b
    def peri(self):
        return (2*self.l)+(2*self.b)

'''    
l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
area_peri = rectangle(l,b)
print("Area of the rectangle is: ",area_peri.area(),"\nPerimeter of the rectangle is : ",area_peri.peri())'''

# Question 2: Create a class called student with the private attributes name, age, marks.
#             Also which checks if the student is eligible for promotion or not.

class student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
    def promotion(self):
        if self.marks >= 40:
            print("Promoted")
        else:
            print("Not promoted")

name = input("Enter name: ")
age = int(input("Enter age: "))
marks = int(input("Enter marks: "))
student_promotion = student(name,age,marks)
student_promotion.promotion()