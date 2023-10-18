def power(x,n):
    pow = 1
    for i in range(n):
        pow *= x
    return pow
x=int(input("x = "))
n=int(input("n = "))
print(power(x,n)/power(x,n+1))