# Q4 print leftmost even number of a list.

list = input("Enter the list ").split()

for i in range(len(list)):
    list[i] = int(list[i])
    if (list[i]%2 == 0):
        print(list[i])
        break