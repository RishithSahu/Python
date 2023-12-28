
class computer:
    def __init__(self,ram,memory):
        self.ram = ram
        self.memory = memory
        print("Computer is ready to use")

class mobile(computer):
    def __init__(self,ram,memory):
        super().__init__(ram,memory)
        print("Mobile is ready to use")
        self.model = "Iphone 15"
        print("Mobile is ready to use")

# m = mobile("16GB","2TB")
# print(m.__dict__)

class person:
    def __init__(self,name,age):
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")
        print("I am",self.name,"and my age is",self.age)
class employee(person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.emp_id = input("Enter your employee id: ")
        self.salary = input("Enter your salary: ")
        print("My employee id is",self.emp_id,"and my salary is",self.salary)
class manager(employee):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age, emp_id, salary)
        self.bonus = input("Enter your bonus: ")
        print("My bonus is",self.bonus)

m = manager()
print(m.__dict__)