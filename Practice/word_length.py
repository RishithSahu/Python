# Python program to print total length of words in a string.

str = input("Enter the string :")
count = 0
for i in str:
    if i == ' ':
        continue
    else:
        count+=1
print(count)