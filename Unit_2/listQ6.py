# Q6 Print difference between successive elements of a list.

list = input("Enter the list ").split()
list2 =[]
for i in range(len(list)):
    list[i] = int(list[i])
    
    list2.append(list[i]-int(list[i+1]))
    print(list2[i])