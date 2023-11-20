#                             MODULES

'''
    Modules are files containing Python code. This code can be
    functions, classes, or variables. This code can be used in other files.
'''
# Question 1 : WAM which reverses the contents of a list.
# Question 2 : WAM which rmoves an item from a list.
# Question 3 : WAM which appends an element in the list.

def reverse_list(lis):
    return lis[::-1]

def remove_item(lis, item):
    lis.remove(item)
    return lis

def append_item(lis, item):
    lis.append(item)
    return lis