# Q5 given a list add a number n to each element.

list = input("Enter the list ").split()
n = int(input("Type n "))
for i in range(len(list)):
    list[i] = int(list[i])
    list[i] = list[i] + n
print(list)
    