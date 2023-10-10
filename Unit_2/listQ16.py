# Q16 Sum of all index in new list.

list = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(list)):
    sum = 0
    for j in range(len(list)):
        list[i][j] = list[i][j]+list[i][2]+list[i][3]
print(list)
    