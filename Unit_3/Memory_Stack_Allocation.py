# In python, function calls and the refrences are stored in stack memory.
# It happens in contigous blocks of memory called Function Call Stack.
# This memory is deleted once the function returns.

# WAP to print the gcd of two numbers.

def gcd(m,n):
    if m==n:
        res = m
    elif m>n:
        res = gcd(m-n,n)
    else:
        res = gcd(m,n-m)
    return res
a = int(input("First number "))
b = int(input("Second number "))
print("The GCD is ",gcd(a,b))