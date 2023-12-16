import tkinter
from tkinter import *
from tkinter import messagebox
import sqlite3

root = tkinter.Tk()
root.resizable(False, False)
root.title('Library Management System - Update')

bk = sqlite3.connect('Bookmaster.db')
bkk = bk.cursor()
st = sqlite3.connect('Studentmaster.db')
std = st.cursor()

global copies
copies = 10

width = 620
height = 320
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))



Label(root, text='WELCOME ADMIN', width=50).grid(row=0, column=1)
Label(root, text='', width=50).grid(row=1, column=1)
l1 = Label(root, text='Enter book title:', width=30).grid(row=2, column=0)
l2 = Label(root, text='Enter book ISBN:', width=30).grid(row=3, column=0)
l3 = Label(root, text='Enter book author:', width=30).grid(row=4, column=0)
Label(root, text='', width=50).grid(row=5, column=1)
e1 = Entry(root, width=50)
e1.grid(row=2, column=1)
e2 = Entry(root, width=50)
e2.grid(row=3, column=1)
e3 = Entry(root, width=50)
e3.grid(row=4, column=1)

l4 = Label(root, text='Enter student name:', width=30).grid(row=8, column=0)
l5 = Label(root, text='Enter student SRN:', width=30).grid(row=9, column=0)
l6 = Label(root, text='Enter card number:', width=30).grid(row=10, column=0)
Label(root, text='', width=50).grid(row=13, column=1)
Label(root, text='', width=50).grid(row=11, column=1)
Label(root, text='', width=50).grid(row=7, column=1)
e4 = Entry(root, width=50)
e4.grid(row=8, column=1)
e5 = Entry(root, width=50)
e5.grid(row=9, column=1)
e6 = Entry(root, width=50)
e6.grid(row=10, column=1)


# Create database
# Comment if already created
# """
# create_Bookmaster = '''CREATE TABLE Bookmaster (
#     Book_Title VARCHAR(255),
#     Book_ISBN INT,
#     Author VARCHAR(255),
#     Copies_Available VARCHAR(255)
# )'''
# bkk.execute(create_Bookmaster)
# create_Studentmaster = '''CREATE TABLE Studentmaster (
#     Student_Name VARCHAR(255),
#     Student_SRN VARCHAR(255),
#     Card_Number INT,
#     Books_Borrowed INT
# )'''
# std.execute(create_Studentmaster)
# """

# Graphics
class book:
    def __init__(self, title, ISBN, author, copies):
        self.title = title
        self.ISBN = ISBN
        self.author = author
        self.copies = 'Available'

    def update(self):
        bk = sqlite3.connect('Bookmaster.db')
        bkk = bk.cursor()
        bkk.execute('''INSERT INTO Bookmaster (Book_Title, Book_ISBN, Author, copies_Available) VALUES (?,?,?,?)''', (self.title, self.ISBN, self.author, self.copies))
        messagebox.showinfo(message='Bookmaster updated.')
        bk.commit()
        bk.close()

class student:
    def __init__(self, name, SRN, cardNumber, count):
        self.name = name
        self.SRN = SRN
        self.cardNumber = cardNumber
        self.count = 0

    def update(self):
        st = sqlite3.connect('Studentmaster.db')
        std = st.cursor()
        std.execute('''INSERT INTO Studentmaster (Student_Name, Student_SRN, Card_Number, Books_Borrowed) VALUES (?,?,?,?)''', (self.name, self.SRN, self.cardNumber, self.count))
        messagebox.showinfo(message='Studentmaster updated.')
        st.commit()
        st.close()

def createBook():
    try:
        Book = book(title=e1.get(), ISBN=int(e2.get()), author=e3.get(), copies='Available')
        Book.update()
    except:
        messagebox.showerror("Value Error",'Please enter valid values.')
    finally:
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)

def createStudent():
    try:
        Student = student(name=e4.get(), SRN=e5.get(), cardNumber=int(e6.get()), count=0)
        Student.update()
    except:
        messagebox.showerror("Value Error",'Please enter valid values.')
    finally:
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)



BKK = Button(root, text='Update Book Data', padx=12, pady=2, command=createBook).grid(row=6, column=0, columnspan=2)
STD = Button(root, text='Update Student Data', padx=12, pady=2, command=createStudent).grid(row=12, column=0, columnspan=2)
bk.commit()
st.commit()
bk.close()
st.close()

root.mainloop()