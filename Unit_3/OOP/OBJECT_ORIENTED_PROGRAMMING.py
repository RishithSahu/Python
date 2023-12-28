#                          OBJECT ORIENTED PROGRAMMING
'''
   Programming paradigm:
   Programming paradigm refers to the style or way in which we write programs.
   The two main ways are procedural programming and object oriented programming.

   Procedure Orinted Programming:
   It mainly focuses on procedures. A procedure is a set of instructions used to acomplish a task.
   It can be routines , subroutines or functions, etc.
   It is also called structured programming.
   It is still used to devloup small programs.

   Obect Oriented Programming:
   Obect Oriented Programming is a programming paradigm that focuses on organising
   and design code by representing real world entities as objects.
   Here the main focus is on the data and the operations that mainpulate the data.
   In Python, we can create objects that contain both attributes(data)
   and methods(functions).
   OOP was devlouped to overcome the drawbacks of procedural programming.
'''
# CLasses : A class is a blueprint for the object.(Blue print of a house)
# Objects : An object is an instance of a class.(The house)
# Attributes : An attribute is a characteristic of an object.(The construction components of the house)
# Methods : A method is an operation we can perform with the object.(The process of building the house)
'''
   Data Abstraction : It refers to the act of representing 
   essential features without including the background details or explanations.

   Data Encapsulation : The wraping up of data and functions into a single 
   unit is known as encapsulation. Encapsulation is a way to achieve data abstraction.
'''

'''
            >attributes/data/fields
           /
   Class -
           \
            >methods/functions
'''

# Modularity : Partioning a program into individual components is called modularity.
''' Inheritance : It is the capability of one class to derive or inherit the properties
    from another class. The child class will inherit the properties of the parent class.'''
'''Polymorphism : It is the concept that supports the capability of an object to behave
   differently in response to the message or data.'''

# print(Sample)
# print(type(Sample))
# print(id(Sample))
# <class '__main__.Sample'>
# <class 'type'>
# 2338595987536

class Sample:
      a = 10
      b = 20
      def display(self):
            print("This is my first oop program")      

print(Sample.a,Sample. b)
Sample.display(self=Sample)


# Create a object called s, and also call display() method

s = Sample()
s.display()
print(s.a,s.b)

# Create a class called student with data members student_no, name, marks, create
# a function called display which says "END OF SEMISTER"

class Student:
      student_no = 101
      name = "Nagarjun"
      marks = 100
      def display(self,marks):
            if marks >= 99:
                  print("Nagarjun got A+ grade")
            print("END OF SEMISTER")

s = Student()
print(s.student_no,s.name,s.marks)
s.display(s.marks)