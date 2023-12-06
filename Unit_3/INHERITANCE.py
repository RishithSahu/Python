#                           INHERITANCE

'''
class Employee:
    emp_sal = 100000
    def display(self):
        print("Employee class this is indeed")

class Manager(Employee):
    def display(self):
        print("Manager class this is certainly")

e = Employee()
e.display()
print(e.emp_sal)

m = Manager()
m.display()
print(m.emp_sal)
'''
# Simple Inheritance

class Parent:
    def __init__(self):
        self.name = input("Enter your name: ")
        print("Parent")

class Child(Parent):
    def __init__(self):
        super().__init__()  # Call the parent class constructor
        self.name = input("Enter your name: ")
        print("Child")

c = Child()
print(c.__dict__)