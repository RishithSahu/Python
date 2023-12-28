# WAP to create two base classes called add and mult , derive a classs called 
# called derived from the aove two laseese and display the result of multipication
# from an object of a derived class.

class add:
    def __init__(self ,c,d):
        self.a=c
        self.b=d
    def addd(self):
        return self.a+self.b
    
class mult:
    def __init__(self ,a,b):
        self.a=a
        self.b=b
    def multi(self):
        return self.a*self.b
    
class derived(add,mult):
    def __init__(self ,a,b):
        super().__init__(a,b)
    def display(self):
        print("The multiplication is : ",self.multi())
        print("The addition is : ",self.addd())

d=derived(10,20)
print(d.display())