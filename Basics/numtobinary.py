# Write a program to convert decimal to binary.

num=int(input("Enter a number = "))
result =""
while num!=0:
	remain=num%2
	num=num//2
	result=str(remain)+result
print("Binary number is = ",result)
