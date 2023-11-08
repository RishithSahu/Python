#                                             RECURSION
'''When the same function calls itself it is called a recursive function.
It reduces the length of the code.
''' 

def fact(x):
    if x==0:
        return 1
    else:
        factoriaal=x*fact(x-1)
        return factoriaal

n = int(input("Enter nummber : "))
print(fact(n))