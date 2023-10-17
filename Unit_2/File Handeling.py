#                                            File Handeling
''' Python3 demo.py 2 3   -->(command line argument)
Using input() function.
These input types are limited therefore we need file handeling,
-The data can be much larger
-Less errors and quickly
-Data is persistent

> Open a file
> Read or write
> Close the file(Compulsory)
'''
Fo = open(r"D:\Rishith\Python\Unit_2\demo.txt",mode='a')
# d = Fo.read()   #Reads the contents of a file
# print(d)
# e = Fo.readline()   #Reads the first line of a file
# print(e)
# f = Fo.readlines()   #Reads the lines of a file
# print(f)                                             '''Only one works at a time'''
e = Fo.write("\nTis very new technology")
# print("Tell me the truth ",file=Fo)     # Prints it in the file
For = open(r"D:\Rishith\Python\Unit_2\demo.txt",mode='r')
d = For.read()
print("The truth is ....... \n",d)
Fo.close()