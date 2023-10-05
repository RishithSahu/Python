# Printing every element reverse
t1 = 1,2,3,"Python",5
print(t1[::-1])
print(t1[-5:-1])


# nested tuple
t2 = 10,11,12,(13,14,15)
print(t2[3][1])

'''(0[10])(1[11])(2[12])(3[(0[13])(1[14])(2[15])])'''

''' tuples are imuaetable
t1.append(6)
t1.insert(6)'''

# Tuples are ordered
tt = 1,2,3
ty = 1,3,2
print(tt == ty)