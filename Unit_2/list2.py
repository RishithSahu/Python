# Given a list , the elements of the print the list in a aseperate line
list = input("Enter the list ").split()

for i in range(len(list)):
    list[i] = int(list[i])
print(list)