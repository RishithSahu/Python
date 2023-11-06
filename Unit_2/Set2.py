list = [1,2,3,4,5]
tup = {11,12,13,14,1,2,3,4}
se1 = {1,2,3,4,5,6,8.2344,9,10}
print(type(tup))
print(type(se1))

print(all(se1))   # Checks if all elements are True or False
print(any(se1))   # Checks if any elements are True
sorted(se1)
se1.pop()
print(se1)
#se1.remove(8) throws an error
se1.discard(3)
se1.remove(4)  
print(se1)

print(se1|tup)
print(se1.intersection(tup)) # puts the intersection in the new set
print(se1.intersection_update(tup)) # puts the intersection in the same set se1
print(se1)

print(se1-tup)
print(se1.difference(tup))
print(se1.difference_update(tup))
print(se1)

