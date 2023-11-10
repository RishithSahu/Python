#                                                     DECORATORS
''' A powerful and useful tool in python since it 
    allows you to modify the behavior of function or class
 '''
''' Decorators wrap a function and modify its behavior in 
    one or the other way without changing the source code.

    Function and then called inside the wraper function
    in decoration functions are taken as the argument into another 
    
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