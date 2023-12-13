def add(x,n):
    if n==0:
        return x
    elif x==0:
        return n
    else:
        return add(x+1,n-1)
print(add(2,3))
def sub(x,n):
    if x==0:
        return n
    else:
        return sub(x-1,n-1)
print(sub(2,3))