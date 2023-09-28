# WAP to print number divisible by 3 and 5.
n1=int(input("Starting number "))
n2=int(input("Ending number "))

for i in range(n1,n2):
   if(i%3==0 and i%5== 0):
      print(i)