# Q2 :- Given empty list , insert n elements in a list

list = input("Enter the list ").split()
numofterms = int(input())

for i in range(numofterms):
    list.append(i)
    print(list[i])