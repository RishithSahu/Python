# WAP to print the tower of hanoi.

def tower(n,src,aux,dest):
    if n == 1:
        print("Move disk 1 from source",src,"To destination",dest)
        return tower(n-1,src,dest,aux)
    print("move disk",n,"from source",src,"to destination",dest)
    tower(n-1,aux,src,dest)
    n = int(input("Enter the number of disks : "))
    tower(n,'A','B','C')