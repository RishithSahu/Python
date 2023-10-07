# String - 2

# Escape sequence
str1 = "Yo \"Python!\""
print(str1)

# \n ...... We know

# A comment
str2 = '''
A multi \
line comment. \
I didn't know!!!\
'''
print(str2)

print(len(str2))

for eleph in str2:
    print(eleph)    # Puting (end = "") will print everything in one line unlike this

for i in range(len(str2)):
    print(i,str2[i])