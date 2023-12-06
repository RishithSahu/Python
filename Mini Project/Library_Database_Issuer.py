import csv
import datetime
import pandas as pd
from tkinter import *
import tkinter.messagebox

root = Tk()

choice = "n"
SRN = 0
ISBN = 0

def Yes():
    global choice
    choice = "y"
def No():
    global choice
    choice = "n"
def Clear():
    e1.delete(0, END)
    e2.delete(0, END)
def Submit():
    global ISBN
    global SRN
    ISBN = e1.get()
    SRN = e2.get()
    tkinter.messagebox.showinfo("Success", "Book Issued.")
def Exit():
    global ISBN
    global SRN
    ISBN = e1.get()
    SRN = e2.get()
    tkinter.messagebox.showinfo("Success", "Book Issued.\n       Bye!")
    root.quit()


# Label Widgets

myLabel1 = Label(root, text = "Welcome Admin").grid(row = 0, column = 0)
myLabel2 = Label(root, text = "           Enter your ISBN :").grid(row = 3, column = 0)
myLabel3 = Label(root, text = "           Enter your SRN :").grid(row = 4, column = 0)
myLabel4 = Label(root, text = "Do you wish to continue?      ").grid(row = 5, column = 0)

# Entry Widgets
e1 = Entry(root, width = 30, borderwidth = 5)
e1.grid(row = 3, column = 1)
e2 = Entry(root, width = 30, borderwidth = 5)
e2.grid(row = 4, column = 1)

# Button Widgets

b1 = Button(root, text = "Yes",command=lambda : [Yes(),Submit(),Clear()], padx = 5, pady = 1, bg = "green", fg = "white").grid(row = 5, column = 1)
b2 = Button(root, text = "No",command=lambda : [No(), Exit()],padx = 5, pady = 1, bg = "red", fg = "white").grid(row = 5, column = 2)


root.mainloop()

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
        current_date_time = datetime.datetime.now()
        row.append([sl_no, ISBN, SRN, current_date_time])
        sl_no += 1
        csvwriter.writerows(row)
        edit_bkk(int(ISBN))
        edit_std(int(SRN))
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