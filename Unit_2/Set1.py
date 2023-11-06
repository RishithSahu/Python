'''                                            SET

Set is an UNORDERED collection of elements with zero or more elements present.
It is - mutable,hashable,iterable
Hashable : hash(23) will give 23, hash(2,3) will give an output ____, 
append()-->add()
remove(43)--->has an error if 43 not in set
discard()---> no error
pop()---> removes a random element
no repetation----> print(s1*3)[Error]

'''
print(hash(12))
x = 34
y = (2,3)
print(hash(x))
print(hash(y))

list = [1,2,3,4,5]
tup = 11,12,13,14
se1 = {1,2,3,4,5,6,"Python",8.2344,9,10}
print(se1)
for i in se1:
    print(i)
se1.add(tup)     # Only 1 argument
print(se1)
se1 = {1,2,3,4,5,6,8.2344,9,10}
# se1.add(list)  A list is not hashable(Only immutable things can be added) 
print(len(se1))
print(max(se1))
print(min(se1))
print(sum(se1))