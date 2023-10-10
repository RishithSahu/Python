# Q9 Create a new list which is sorted

list = input("Enter the list ").split()
list2 = []

for i in range(len(list)):
    for j in range(len(list)):
        if (list[i]>list[j]):
            list2.append(list[i])
        elif (list[i]<list[j]):
            list2.append(list[i])

for i in range(len(list)):
    if list[i] not in list2:
        list2.append(list[i])
        
print(list2)
'''Its best to use .sort()'''