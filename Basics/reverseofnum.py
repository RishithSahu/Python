# A program to reverse a number.

num  = int(input("Enter Number "))
reverse = 0
if num == 0:
     print("Number is 0")

while (num!=0):    # This loop will run until num is not equal to 0.
     rem=num%10
     num//=10
     reverse=reverse*10+rem
     print(reverse)

print("Reverse of the number is ",reverse)