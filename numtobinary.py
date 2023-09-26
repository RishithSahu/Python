# Write a program from decimal to binary.

num=int(input("Enter a number = "))
res =""
while num!=0:
	rem=num%2
	num=num//2
	res=str(rem)+res
print("Binary number is = ",res)
