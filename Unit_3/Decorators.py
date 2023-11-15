#                                                     DECORATORS
''' A powerful and useful tool in python since it 
    allows you to modify the behavior of function or class
 '''
''' Decorators wrap a function and modify its behavior in 
    one or the other way without changing the source code.

    Function and then called inside the wraper function
    in decorators functions are taken as the argument into another 
    
    It takes input as a function and outputs a function too.
'''

def feuncdec(func):
    def inner():
        print("Hello before")
        func()
        print("Hello after")
    return inner
def hello():
    print("inside Hello")

hello = feuncdec(hello)
hello()

# Write a function which divides a/b. Use a decorative function to validate for 
# division error(denominator cannot be zero)

def deco(func):
    def inner(a,b):
        if b == 0:
            return "Division Error"
        else:
            func(a,b)
    return inner
@deco
def division(a,b):
    return a/b

a = int(input("Enter a : "))
b = int(input("Enter b : "))

print(division(a,b))
