# WAP to print factor of a number.
num = int(input("Enter the number "))
for i in range(1,num):
    if num%i == 0 and i != 1:
        print(i)