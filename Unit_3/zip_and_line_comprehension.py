#         Higher order functions
#              ZIP
'''
   The zip function takes iterable containers and returns a single iterator object
   having mapped values from all the containers.

   It is used to map the similar index of multiple containers so that they can be used
   just using as single entity.
   
   Syntax: zip(*iterators)

   The zip function is used to associate the corresponding elements of two or more
   iterables into a single lazy iterator.
'''

name = ['John', 'Peter', 'Mathew']
roll_no = [23, 45, 56]
mapped = list(zip(name, roll_no))
print(mapped)

lst1 = [1,2,3,4,5]
lst2 = list(map(lambda x:x*x*x, lst1))
mapped = list(zip(lst1,lst2))
print(mapped)

'''                                 List comprehension
    It is a way to create a consise list in python.
    It is used to create functionality withini a single line statement.
    
'''
# lst = input("Enter the list: ").split()
# new_lst = [int(x) for x in lst]

# lst2 = input("Enter the list: ").split()
# new_lst2 = [a for a in lst]
# print(new_lst2)

# Question 1: WAP to convert a list into uppercase.

'''
lst = input("Enter the list: ").split()
new_lst = [x.upper() for x in lst]
print(new_lst)'''

# Question 2: WAP to print all the cities whose length is greater than or equal to 6.
'''
cities = ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai', 'Kolkata']
true_cities = [x.upper() for x in cities if len(x)>=6]
print(true_cities)
  
print([(x,len(x)) for x in ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai', 'Kolkata'] if len(x)>=6])
'''

# Question 3: WAP to print a list which contains 1 to 10 and list 2 sholud contain even numbers from list 1.

# print([x**2 for x in range(1,11) if x%2==0]) 

# lst1 = [1,2,3]
# lst2 = ['a','b','c']
# print([(lst1[x],lst2[y]) for x in range(len(lst1)) for y in range(len(lst2)) if x==y ])

# fruits = ['apple', 'banana', 'cherry', "kiwi", "mango", "orange", "watermelon", "grapes", "papaya", "pineapple"]
# Question 4: WAP to print a list which contains a in the list of fruits.

# print([x for x in fruits if 'a' in x])

# Question 5: WAP to print all numbers 1 to 100 if it    is divisible by 2 and 5.

# print([x for x in range(1,101) if x%2==0 and x%5==0])

# Question 6: WAP to take n and print n different values

# n = int(input())
# print([x for x in range(1,n+1)])