# Write a program to print grade A>70, print grade B>50, print grade C>35, print FAIL.
marks = int(input("Enter marks "))

if marks >= 70:
    print("Grade A")
elif marks >= 50:
    print("Grade B")
elif marks >= 35:
    print("Grade C")
else:
    print("FAIL")
 