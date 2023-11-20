import csv
import datetime
import pandas as pd

def edit_bkk(ISBN):
    with open("D:\Rishith\Python\Mini Project\Library_Database_Manager_Bookmaster.csv",'r') as file:
        csvreader = csv.reader(file)
        data = []
        for lines in csvreader:
            if ISBN in lines:
                lines[4] = 'Borrowed'
            else:
                pass
            data.append(lines)
    with open("D:\Rishith\Python\Mini Project\Library_Database_Manager_Bookmaster.csv",'w', newline='') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerows(data) 

def edit_std(SRN):
    with open("D:\Rishith\Python\Mini Project\Library_Database_Manager_Studentmaster.csv",'r') as file:
        csvreader = csv.reader(file)
        data = []
        for lines in csvreader:
            if SRN in lines:
                lines[4] += 1
            else:
                pass
            data.append(lines)
    with open("D:\Rishith\Python\Mini Project\Library_Database_Manager_Studentmaster.csv",'w', newline='') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerows(data)

with open("D:\Rishith\Python\Mini Project\Library_Database_Issuer.csv",'a') as file:
    sl_no = 0
    csvwriter = csv.writer(file)
    if sl_no == 0:
       csvwriter.writerow(["SL NO.", "ISBN", "STUDENT SRN", "ISSUE DATE"])
    while True:
        row = []
        ISBN = input("Enter book ISBN: ")
        SRN = input("Enter student SRN: ")
        current_date_time = datetime.datetime.now()
        row.append([sl_no, ISBN, SRN, current_date_time])
        sl_no += 1
        csvwriter.writerows(row)
        edit_bkk(int(ISBN))
        edit_std(int(SRN))
        choice = input("Continue? (y/n): ")
        print()
        if choice == 'y':
            continue
        elif choice =='n':
            break
        else:
            print("Enter valid input: ")
            break


dataframe1 = pd.read_csv("D:\Rishith\Python\Mini Project\Library_Database_Issuer.csv")
dataframe1 = dataframe1[["ISBN"]]
dataframe1.to_csv("D:\Rishith\Python\Mini Project\Library_Database_ISBN.csv", index=False)

dataframe2 = pd.read_csv("D:\Rishith\Python\Mini Project\Library_Database_Issuer.csv")
dataframe2 = dataframe2[["STUDENT SRN"]]
dataframe2.to_csv("D:\Rishith\Python\Mini Project\Library_Database_SRN.csv", index=False)