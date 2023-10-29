# Write a program to print grade A>70, print grade B>50, print grade C>35, print FAIL.
marks = input("Enter marks ").split()
for i in range(len(marks)):
    marks[i] = int(marks[i])
    if marks[i] >= 90:
       print("Grade A")
    elif marks[i] >= 80:
       print("Grade B")
    elif marks[i] >= 70:
       print("Grade C")
    elif marks[i] >= 60:
       print("Grade D")
    else:
       print("FAIL")