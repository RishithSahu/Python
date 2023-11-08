#                                             RECURSION
'''When the same function calls itself it is called a recursive function.
It reduces the length of the code.

''' 

def fact(x):                    # Function Header
    if x==0:                    # Base Condition
        return 1                # Base Condition
    else:
        factoriaal=x*fact(x-1)
        return factoriaal

print(fact(4))

# to find sum using recurssion.
sum = 0
def summ(a,b):
   if b==0:
      return a
   return (summ(a,b-1) + 1)
print(summ(2,3))

# WAP to find difference
def diff(a1,b1):
   if b1==0:
      return a1
   return diff(a1-1,b1-1)
print(diff(20,3))

# WAP to fing multiplication
def multi(a,b):
   if b==0:
      return 0
   return (multi(a,b-1)+a)

print(multi(1,23))