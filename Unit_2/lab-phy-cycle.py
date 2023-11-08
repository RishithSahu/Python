# Nikhil, M section


# PHYSICS CYCLE

""" 
1) Write a program that takes the number of rows 'n' as input from the user and prints a number
pattern in increasing order as shown below.If n is 5, the expected pattern is,
1
2 3
4 5 6
11 8 9 10
11 12 13 14 15
"""

# n = int(input("Enter the number of rows: "))
# num = 1
# for i in range(1, n + 1):
#     for j in range(i):
#         print(num, end=" ")
#         num += 1
#     print()

"""
2) Write a program that takes the number of rows 'n' as input from the user and prints a diamond
pattern using asterisks (*) as shown in the sample example. Note that input ‘n’ will be an odd
integer. The pattern should have a diamond shape with 'n' rows in the middle.If n is 5, the
expected pattern is,
  *
 ***
*****
 ***
  *
"""

# while True:
#     n = int(input("Enter the number of rows: "))
#     if n % 2 == 0:
#         print("Please enter odd number")
#     else:
#         break

# t = (n + 1) // 2

# for i in range(1, n + 1):
#     print(" " * abs(t - i), end="")
#     print("*" * ((t - abs(t - i)) * 2 - 1))

""" 
3) Write a program that calculates and prints the Least Common Multiple (LCM) of two
positive integers entered by the user.
"""

# n1 = int(input("Enter the first number: "))
# n2 = int(input("Enter the second number: "))

# print(
#     "LCM of",
#     n1,
#     "and",
#     n2,
#     "is",
#     sorted(
#         list(
#             set([i * n2 for i in range(1, n1 + 1)]).intersection(
#                 set([i * n1 for i in range(1, n2 + 1)])
#             )
#         )
#     )[0],
# )


""" 
4) Write a program that prompts the user to input a positive integer, checks if it's a valid positive
integer, and then determines whether it's an Armstrong number.If the user enters a negative
number or a non-integer value, provide an appropriate message. The program should display
whether or not the input is an Armstrong number.An Armstrong number is one where the sum
of its individual digits, each raised to the power of the number of digits in the original
number, equals the original number (e.g., 153 is an Armstrong number because 1^3 + 5^3 +
3^3 = 153).
"""

# while True:
#     n = input("Enter a positive integer: ")
#     if n.isdigit():
#         n = int(n)
#         if n > 0:
#             n = str(n)
#             break
#         else:
#             print("Please enter a positive integer")
#     else:
#         print("Please enter a positive integer")

# print(
#     f"{n} is an Armstrong number"
#     if sum([int(i) ** len(n) for i in n]) == int(n)
#     else f"{n} is not an Armstrong number"
# )

""" 
5) Write a program that accepts a square 2D list (nested list/like matrix) representing a grid of
integers from the user. Calculate and print the sum of the elements along both the main
diagonal (top-left to bottom-right) and the secondary diagonal (top-right to bottom-left) of the
2D list(nested list/ like matrix)
"""

# n = int(input("Enter the number of rows: "))

# mat = [int(input("Enter the element at {i},{j}: ")) for j in range(n)] for i in range(n)
# print(mat)
# d1, d2 = 0, 0
# for i in range(n):
#     d1 += mat[i][i]
#     d2 += mat[i][n - i - 1]
# print(f"Sum of elements along the main diagonal is {d1}")
# print(f"Sum of elements along the main diagonal is {d2}")


"""
6) Write a program that accepts a square 2D list (nested list/like matrix) representing a grid of
integers from the user. Find and print the maximum value in the entire 2D list(nested list/ like
matrix) along with its row and column indices.
"""

# n = int(input("Enter number of rows: "))

# mat = [[int(input(f"Enter element at {i},{j} : ")) for j in range(n)] for i in range(n)]

# m = max([max(i) for i in mat])
# for i in range(n):
#     if mat[i].index(m) != -1:
#         print(f"Maximum element is {m}, and it occupies index {i,mat[i].index(m)}")


"""
7) Write a program that accepts a square 2D list (nested list/like matrix) representing a grid of
integers from the user. Find and print the minimum value in the entire matrix along with its
row and column indices.
"""

# n = int(input("Enter number of rows: "))

# mat = [[int(input(f"Enter element at {i},{j} : ")) for j in range(n)] for i in range(n)]

# m = min([min(i) for i in mat])
# for i in range(n):
#     if mat[i].index(m) != -1:
#         print(f"Least element is {m}, and it occupies index {i,mat[i].index(m)}")

""" 
8) Write a program that takes an integer ‘n’ as the number of elements and an integer ‘k’ as the
desired occurrence frequency from the user. The program should remove all elements that
occur exactly k times from the list and print the modified list. Both ‘n’ and ‘k’ are positive
integers and k <= n.
Eg: n=7, input_lst=[10,20,20,30,40,10,50], k=2 Output=[30,40,50]
"""

# n = int(input("Enter number of elements: "))

# input_lst = []

# for i in range(n):
#     input_lst.append(int(input("Enter a digit: ")))

# k = int(input("Enter frequency to delete: "))

# for item in set(input_lst):
#     if input_lst.count(item) == k:
#         input_lst = [j for j in input_lst if j != item]

# print(f"Output = {input_lst}")

"""
9) Write a program that takes an integer 'n' as the number of elements and an integer 'k' as the
desired occurrence frequency from the user. The program should remove all elements that do
not occur exactly 'k' times within the list and print the resulting modified list. Both ‘n’ and ‘k’
are positive integers and k <= n.
Eg: n=7, input_lst=[10,20,20,30,40,10,50], k=2 Output=[20,20,10,10]
"""

# n = int(input("Enter number of elements: "))

# input_lst = []

# for i in range(n):
#     input_lst.append(int(input("Enter a digit: ")))

# k = int(input("Enter frequency to keep: "))
# temp = []
# for item in set(input_lst):
#     if input_lst.count(item) == k:
#         temp += [j for j in input_lst if j == item]

# print(f"Output = {temp}")

""" 
10) Write a program that takes a string ‘test_str’ and a substring ‘sub_str’ as inputs from the user.
Find the sub_str that occurs the most in a list of words formed by splitting test_str into words.
For Example, if the test_str string is "This is a test string testtest" and sub_str is "test". Then
the output would be "testtest" as the sub_str has been repeated twice.
"""

# test_str = input("Enter string: ").split()
# sub_str = input("Enter substring to check: ")

# d = dict(
#     zip(
#         [int(len(i.split(sub_str)) - 1) for i in test_str],
#         [i for i in test_str],
#     )
# )
# print(d[max(d.keys())])

"""
11) Write a Python program that takes two strings as inputs from the user and checks if one string
is a rotation of another string. For example, "waterbottle" is a rotation of "erbottlewat". Your
program should print 'Y' if one string is a rotation of the other, and 'N' if it is not.
"""

# s1 = input("Enter the first string: ")
# s2 = input("Enter the second string: ")

# if len(s1) != len(s2):
#     print("N")
# else:
#     for i in range(len(s1)):
#         s2 = s2[i:] + s2[:i]
#         if s2 == s1:
#             print("Y")
#             break
#     else:
#         print("N")

# OR

# n = input()
# rn = input()
# newn = n*2
# if rn in newn:
#     print("Y")
# else:
#     print("N")

""" 
12) Write a Python program that takes a string as input, finds and prints all the unique substrings
of the given string in a list in lexicographical order
"""

# st = input("Enter string: ")

# l = []

# for i in range(len(st)):
#     for j in range(i, len(st)):
#         l.append(st[i : j + 1])

# print(sorted(set(l)))

""" 
13) Write a Python program that takes two strings as inputs from the user and checks if one string
is an anagram of the other string.Your program should print 'Y' if one string is an anagram of
the other, and 'N' if it is not. An anagram is a word or phrase formed by rearranging the letters
of another word or phrase, using all the original letters exactly once. For instance, if the first
string is "listen" and the second string is "silent", the program should print ‘Y’. Another
example for anagram is "race" and "care" and thus the program should print ‘Y’ for this input
as well.
"""

# st = list(input("Enter normal string: "))
# st2 = list(input(f"Enter new string to check if it's an anagram: "))

# for i in st2:
#     if i in st:
#         st.remove(i)

# if len(st) == 0:
#     print("Y")
# else:
#     print("N")

""" 
14) Write a Python program that calculates the sum of numerical values assigned to each letter in
a given string, where 'a' is assigned the value 1, 'b' is assigned the value 2, and 'z' is assigned
the value 26. For instance, if the input string is "hello," the program should calculate the sum
as follows: 'h' (8) + 'e' (5) + 'l' (12) + 'l' (12) + 'o' (15) for a total sum of 52. The program
should then display the calculated sum as the result.
"""

# while True:
#     st = input("Enter string: ")
#     if not (st.isalpha()):
#         print("Enter only alphabets")
#     else:
#         break

# sum = 0

# for i in st:
#     sum += ord(i.lower()) - 96

# print(sum)

""" 
15) Write a program that takes a sentence as input from the user and converts each alphabet in a
given sentence to the next letter in the alphabet, while preserving the case of the letters and
prints it. For example, a is converted to b, b to c, so on and z to a.If the input is “Hello,
World”, the expected output is “Ifmmp, Xpsme”.
"""

# st = input("Enter string: ")
# newst = ""

# for i in st:
#     if i.isalpha():
#         newst += chr(ord(i) + 1)
#     else:
#         newst += i

# print(newst)


"------------------------------------------------------"


# CHEM CYCLE


""" 
1) Write a Python program that checks if a given non-negative integer from the user, is a
palindrome. A palindrome is a number that remains the same when its digits are reversed. For
example, 121 is a palindrome because it reads the same forward and backward, whereas 1231
is not a palindrome.
"""

# while True:
#     n = input("Enter a non negetive integer: ")
#     if n.isdigit():
#         if int(n) >= 0:
#             break
#         else:
#             print("Non negetive integer only!")
#     else:
#         print("Non negetive integer only!")

# print(f"{n} is a palindrome" if n == n[::-1] else f"{n} is not a palindrome")

""" 
2) Write a program that takes number of rows ‘n’ as input and prints the following pattern. For
n=4, it is,
1
121
12321
1234321
"""

# n = int(input("Enter number of rows: "))

# for i in range(1, n + 1):
#     l = [k for k in range(1, i + 1)] + [k for k in range(i - 1, 0, -1)]
#     print(*l, sep="")

""" 
4) Write a program that takes number of rows ‘n’ as input and prints the following pattern, for
n=4, it is,
1
10
101
1010
"""

# n = int(input("Enter number of rows: "))

# for i in range(1, n + 1):
#     for j in range(i):
#         if j % 2 == 0:
#             print("1", end="")
#         else:
#             print("0", end="")

#     print()


""" 
5) Write a program that takes an integer 'n' as the number of elements to be inserted inside a list.
Accept the integer elements for list from the user and an integer 'k' as the desired occurrence
frequency from the user. The program should remove all elements that do not occur exactly
'k' times within the list and print the resulting modified list.
Eg: n=7, input_lst=[10,20,20,30,40,10,50], k=2 Output=[20,20,10,10]
"""

# REFER TO QUESTION 8 IN PHY CYCLE

""" 
6) Write a program that takes integer 'n' as the number of elements to be inserted inside a list.
Accept the integer elements for list, and position 'k' from the user. The program's objective is
to find and display the kth smallest number from the list. It is important to note that the
numbers in the list may be repeated, and a simple sorting approach may not yield the correct
result. The program should handle this case by considering the frequency of each number.
Eg1:-n=6, lst1=[20,7,15,16,7,8], k=3 output=15
Eg 2:- n=5,lst1=[5,4,19,9,18], k=8 output=None
"""

# n = int(input("Enter number of elements: "))
# lst1 = []
# for i in range(n):
#     lst1.append(int(input("Enter element: ")))

# k = int(input("Kth smallest element: "))

# try:
#     print(list(set(lst1))[k - 1])
# except:
#     print("None")


""" 
7) Write a program that takes integer 'n' as the number of elements to be inserted inside a list,
and the integer elements for list from the user. Modify each element of a list by replacing it
with the sum of the next two elements. Assume the list is circular, so the last element will be
the sum of the elements at index[0] and index[1].
Eg1:-n=4,lst1=[1,2,3,4] output=[5,7,5,3]
Eg2: n=2, lst1=[100,200], output=[300,300]
"""

# n = int(input("Enter number of elements: "))
# lst1 = []
# for i in range(n):
#     lst1.append(int(input("Enter element: ")))
# sum = []
# for i in range(-1, -len(lst1) - 1, -1):
#     sum.append(lst1[i + 1] + lst1[i + 2])

# print(sum[::-1])

""" 
8) Write a program that accepts a square 2D list (nested list/like matrix) representing a grid of
integers from the user and prints the average of the elements along the main diagonal of the
2D list(nested list).
Eg 1: row_ col= 3, input_lst1=[[1,2,3],[4,5,6],[7,8,9]], output= 5.0 (i.e. (1 + 5 + 9) / 3 =5.0)
"""

# n = int(input("Enter number of rows: "))
# mat = [[int(input(f"Enter element at {i,j}: ")) for j in range(n)] for i in range(n)]
# sum = 0
# for i in range(n):
#     sum += mat[i][i]

# print(sum / n)

""" 
9) Write a program that accepts a square 2D list (nested list/like matrix) representing a grid of
integers from the user and print the transpose of the 2D list(nested list/like matrix).
Eg 1:- row_col=3 input_lst1= [[1, 5],[2, 7]] Output= [[1, 2],[5, 7]]
"""

# n = int(input("Enter number of rows: "))
# mat = [[int(input(f"Enter element at {i,j}: ")) for j in range(n)] for i in range(n)]

# l = []

# for i in range(n):
#     temp = []
#     for j in range(n):
#         temp.append(mat[j][i])
#     l.append(temp)

# print(l)

""" 
10) Write a program that takes a sentence as input and converts each alphabet in a given sentence
to the next letter in the alphabet, while preserving the case of the letters. For example, a is
converted to b, b to c, so on and z to a. (ignore punctuations in the input sentence) Eg:
inp_str=”Welcome to python” output=”Xfmdpnf up qzuipm”
"""

# REFER TO Q) 15 IN PHY CYCLE

""" 
11) Write a program to take inputs of different data type as key input and then the value as its
data_types name (i.e,. “string”, “integer” or “float”). Store the values in a dictionary with key
as input and value as data type. Make a sentence with all the inputs which are of string data
type and display the same. For example, for the dictionary {"hello":"string", 5:"integer",
“world”: “string”} the sentence is "hello world".
"""

# n = int(input("Enter number of datatypes-data key:value pairs exist: "))

# d = {
#     key: value
#     for key, value in [
#         (input(f"Enter datatype:element : ")).split(":") for i in range(n)
#     ]
# }

# st = ""
# for i in d.keys():
#     if d[i] == "string":
#         st += i + " "

# print(st)

""" 
12) Write a python program that accepts two inputs as word from the user and checks if two
words are anagrams of each other. An anagram is a word or phrase formed by rearranging the
letters of another.
Eg 1: inp_string 1: anagram inp_string 2: nagaram , Output: True
Eg 2: inp_string 1: baseball, inp_string 2: basketball , Output: False
"""

# REFER TO Q) 13 IN PHY CYCLE

""" 
13) Write a program that accepts word as input from the user and translates that word into Pig
Latin. In Pig Latin, words are transformed by moving the first letter to the end and adding
"ay." For example, "hello" becomes "ellohay."
"""

# s = input("Enter string: ")
# print(s[1:] + s[:1] + "ay")

""" 
14) A cipher is a method of transforming a message to conceal its meaning. The simplest
technique involves shifting the letters in the message by a certain number of positions, known
as the “shift” or “key”. Given a message and an integer shift value, print the encrypted
message. For instance, Encryption - If shift value is 2, A becomes C, B becomes D etc. Z
cycles back and becomes B.
Eg1: inp_str=”Hello world” , shift_value=3, Output= Khoor zruog
Eg2: inp_str=” Zero to hero!” , shift_value=1, Output= Afsp up ifsp!
"""

# s = list(input("Enter string to be cyphered: "))

# n = int(input("Enter shift value: "))

# for i in range(len(s)):
#     if s[i].isalpha():
#         s[i] = chr(ord(s[i]) + n % 26)

# print(*s, sep="")

""" 
15) Write a Python program that takes a string as input, finds and prints all the unique substrings
of the given string in a list in lexicographical order.
"""

# REFER TO Q) 12 IN PHY CYCLE
