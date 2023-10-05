''' Tuple is imutable(cannot change anything inside) rest is same as list
 To create a tuple tuple = () -->[has to be () only]
 Where the user cannot change the data
 Tuple is a pointer like list
 Sorted(tuple) , len(tuple) , min() , max() , list <---> tuple'''


t1=(11,22,33,44,55,66,77)
print(type(t1))
t2 = tuple()
print(type(t2))
t3 = 1,2,3,"Python",5
print(type(t3))
x,y,z,w,v = t3
print(x,y,z,w,v)
print(t3[3])
# using for to print t3

for i in t3:
    print(i,end="\n")

for j in range(len(t3)):
    print(j,t3[j])

# slicing on tuple
# start:stop:step(default +1)
print(t3[0:5:2])