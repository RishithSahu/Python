tup1 = ((1,2,3),(4,5,6),(7,8,9))
tup2 = ((11,21,31),(41,51,61),(71,81,91))
lst = []
for i in range(0,3):
    for j in range(0,3):
        lst.append(tup1[i][j]+tup2[i][j])
print(lst)