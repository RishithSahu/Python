lis = {1,2,3,4,5}
tup = {11,12,13,14,1,2,3,4}
se1 = {1,2,3,4,5,6,8.2344,9,10}

print(se1-tup)
print(se1.difference(tup))
print(se1.difference_update(tup))
print(se1)
print(se1.symmetric_difference(tup))
print(se1.issubset(tup))
print(se1.issuperset(tup))
print(se1.isdisjoint(tup))

print(hash("python"))

lis.clear()  # Emptys the set
print(lis)
del lis
print(lis) # removes set from existance