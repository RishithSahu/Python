#                                 MAP

'''
    map() is a function that takes in two arguments: a function and a sequence iterable.
    map(function, iterable)
'''
# Question 1: WAP using map func which caplitalizes all the elements in the list.
'''lst = input("Enter the list: ").split()
   print(list(map(lambda st:st*2, lst)))'''

# Question 2: WAP using map func which takes a string  consisting of 
'''s=input("Enter the string: ").split()
   print(list(map(lambda st:int(st), s)))'''

#                      LAMBDA

'''
   They are called nameless functions.
   They are called anonymous functions.
   They are called inline functions.
   It can have any number of arguments but only one expression.
   Does not return any value by default.
   They a
'''

# Question 3: WAP that takes a list of numbers and squares them using lambda.

'''str = input("Enter the list: ").split()
print(list(map(lambda st:int(st)**300, str)))'''

# Question 4: WAP which adds correspondings elements from two lists.

'''lst1 = input("Enter the list1: ").split()
lst2 = input("Enter the list2: ").split()
print(list(map(lambda x,y:int(x)+int(y), lst1,lst2)))'''

# Question 5: WAP which squares each even number in a list.

'''def even(n):
    n = int(n)
    if n%2==0:
        return n**2
    else:
        return n

lst = input("Enter the list: ").split()
print(list(map(even(), lst)))'''

'''
   Lazy and Eager objects
    Lazy objects are those objects which are not evaluated immediately.
    Eager objects are those objects which are evaluated immediately.
'''

# Question 6: WAP crearts a list of squares for odd numbers and cube for even numbers.
lst = input("Enter the list: ").split()
print(list(map(lambda x:int(x)**3 if int(x)%2==0 else int(x)**2, lst)))

