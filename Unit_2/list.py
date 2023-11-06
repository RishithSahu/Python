# List Creation
# Homogenous List
a = [10,20,30,40,50,60,70]
print(a)
# Empty List
b = []
print(b)
# Hetrogenous List
c = [1,1.23,"Bannana"]
print(c)
# A list of Fruits, with duplicate entry(allowed)
fruits = ["apple","banana","mango","orange","apple"]
print(fruits)
# a nested list
d= [a,[80,90,100],"Now we know numbers"]
print(d)
# Sliceing Operations
print(a[0])
for i in range(7):
    print(i,a[i])
print(len(a))
# a[-1] is the last element
print(a[-1])
print(a[0:3])
# .reverse flips the whole list forever
a.reverse()
print(a)
a.reverse()
print(a)
# Some operations in list
print(min(a))
print(max(a))
print(sum(a))
print(a)
print(min(fruits))
print(max(fruits))
print(a+[80,90])
print(a*2)
# 30 in a checks if 30 is in a or not
print(30 in a)
print(34 in a)
print(34 not in a)

# A new Hetrogenous list
x = [10,"python",30]
# .append adds an element at the end of the list
x.append(False)
print(x)
# .insert puts something at any index 
x.insert(4,"Hello")       # 4 is the location
print(x)
# .remove will remove any element from the list
x.remove(False)
print(x)
# .pop we will pass index to pop it out
x.pop(0)
print(x)
# Copy the list into another list
y = x.copy()
print(y)
# .clear will empty the list(no try)
print(x.clear())
# .sort() will sort in acending order(Only for integers)
y = [1,2,0,4,6,7,10,9,3,5,8]
y.sort()
print(y)
# .count(val) will check occourence of val in the list
print(y.count(0))
