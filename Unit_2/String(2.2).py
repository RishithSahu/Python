# Immutable
str1 = "Python is a low-level language"

'''
Slicing is the same as in list and tuple.
Everything is the exact same as tuple.
'''
#### Operations ####
print(ord(min(str1)))
print(ord(max(str1)))
# ord prints ASCII value
# Built in functions
#### Starts with 3 parameters ####
print(str1.startswith("yt",1,4)) # startswith selects 'ython' then checks if it starts with yt
print(str1.endswith("e"))
print(str1.startswith("n",-1,-4)) # Dunno how to get true