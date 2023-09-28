# A program to reverse a number.

num  = int(input("Enter Number"))
reverse = 0

while (num!=0):
     rem=num%10
     reverse=reverse*10+rem
     num//=10
print("Reverse of the number = ",reverse)