list = input("Enter the list : ").split()
def reverser(lst):
    lst2=lst[::-1]
    for i in range(len(lst2)):
        lst2[i] = int(lst2[i])
    return lst2
print(reverser(list))