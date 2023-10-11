# Q13 WAP to count all the numbers in a list which is divisible by 3

list = input("Enter the list ").split()
count = 0
for i in range(len(list)):
    list[i] = int(list[i])
    if (list[i]%3 == 0):
        count += 1
print(count)