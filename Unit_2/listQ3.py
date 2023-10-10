# Q3 GL create a new list which containss the square of the list.

list = input("Enter the list ").split()
list2 = []
for i in range(len(list)):
    list[i] = int(list[i])
    list2.append(pow(list[i],2))
print(list2)