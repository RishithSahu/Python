import csv
with open("Emplst.csv",mode = 'w') effefas file:         # File is a file handeler
    w = csv.writer(file)
    # print(type(w))
    w.writerow(["Emp name","Emp salary","Emp age"])
    for i in range(2):
        Emp_name = input("Your name : ")
        Emp_salary = int(input("Your salary : "))
        Emp_age = int(input("Your age : "))
        w.writerow([Emp_name,Emp_salary,Emp_age])
print("Records created sucessfully!")

# For reading csv file
with open("Emplst.csv",'r') as file1:
    r = csv.reader(file1)
    data = list(r)
    for row in data:
        for col in row:
            print(col,"\t",)