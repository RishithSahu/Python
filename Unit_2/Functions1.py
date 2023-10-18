#                                        FUNCTIONS
# A group of statements that can be called repeatedly.
# Built-in and user defined
# Has a function header and body
'''def function_name():
      print(" Hello")
              
function_name()
> Hello       ^--(Parameters)
'''
import math
def calc(a,b):
     return (a+b),(a-b),(a*b),(a/b)
t = calc(4,2)
print(t)

def fact(x):
    if x>0:
        facto = 1
        for i in range (1,x+1) :
              facto *= i
        return facto 
n=int(input())
result = fact(n)/fact(n+1)
print(result)