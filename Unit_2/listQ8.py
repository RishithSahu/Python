# Create list with single elements (remove duplicates)
list = input("Enter the list ").split()
list2 =[]
for i in range(len(list)):
    if list[i] not in list2:
        list2.append(list[i])
        
print(list2)