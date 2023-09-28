# Write a program to print alphabet using for loop with its ASCII.
n = input("Please input a string")
l = len(n)
for i in range(l):
   print(n[i],ord(n[i]))