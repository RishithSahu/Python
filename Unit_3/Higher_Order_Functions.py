'''
   Programming has two types --> Object oriented
                             --> Functional programming
                                  - User defined functions, math functions, 
                                  - Higher order functions
                                        1> map() function(
                                               map(function, iterable)
                                                         )
                                        2> We use it like this
                                            print(list(map(len , lst)))      # Takes iterable and gives iterable
                                               (In this way len function will
                                                 be used on lst and convert it into a new list())
                                         
'''

lst = ["hello","hi","bye"]
print(list(map(len,lst)))

# Usinf a map func. convert the list of strings to uppercase.


print(list(map(lambda x:x.upper(), lst)))