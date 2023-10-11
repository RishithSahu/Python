# Q16 Sum of all index in new list.

list = [[1,2,3],[4,5,6],[7,8,9]]
list2 = []
for i in range(0,3):
    
    for j in range(0,3):
        list[i][j] = int(list[i][j])
        list2.append(list[i][0]+list[i][1]+list[i][2])
print(list2)
    