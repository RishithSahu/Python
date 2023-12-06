# Data Encaptulation

class Example:
   def __init__(self,name):
      self.name = name
   def get_name(self):
      return self.name
   def set_name(self,new_name):
        self.name = new_name

# obl = Example("Abhay")
# print(obl.get_name())
# obl.set_name("Abhay Shyam Kumar")
# print(obl.get_name())

# Question 1: Create a program with a class called Student with private attributes name, age and grades.
# Using the getter and setter methods, for each attribute.The set age should 
# ensure that the age is not less than 0, if it is then reset it to 0.
# The marks sholud be between 0 and a 100, if it is not then reset it to 0.
# Create a method called report that declares the promotion result of the student.
# The program must take input from user.

class Student:
   def __init__(self,name,age,grades):
      self.name = name
      self.age = age
      self.grades = grades
   def set_age(self):
        if self.age < 0:
            self.age = 0
            return self.age
        else:
            return self.age
   def grade_check(self):
       if self.grades >= 0 and self.grades <= 100:
          if self.grades > 50:
              return "Promoted"
          else:

            return "Repeat year"
       else:
           self.grades = 0
           return self.grades
       
name = input("Enter name : ")
age = int(input("Enter age : "))
grades = int(input("Enter the grades : "))
stu = Student(name, age,grades)
print(stu.set_age())
print(stu.grade_check())

# Inheritance : when a class inherits the properties of another class

class Base:
    def display(self):
        print("This is base class")

class Derived(Base):
    def show(self):
        print("This is derived class") 

d = Derived()
d.display()
d.show()