import tkinter
from tkinter import *
from tkinter import messagebox
import sqlite3

root = tkinter.Tk()
root.resizable(False, False)
root.title('LIBDAT - Issue/Return')

iss = sqlite3.connect('Issuer.db')
isk = iss.cursor()
bk = sqlite3.connect('Bookmaster.db')
bkk = bk.cursor()
st = sqlite3.connect('Studentmaster.db')
std = st.cursor()


width = 620
height = 200
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))


Label(root, text='WELCOME ADMIN', width=50).grid(row=0, column=1)
Label(root, text='', width=50).grid(row=1, column=1)
Label(root, text='Enter Book Title:', width=30).grid(row=2, column=0)
Label(root, text='Enter Book ISBN:', width=30).grid(row=3, column=0)
Label(root, text='Enter Student Name:', width=30).grid(row=4, column=0)
Label(root, text='Enter Student SRN:', width=30).grid(row=5, column=0)
Label(root, text='', width=50).grid(row=6, column=1)
e1 = Entry(root, width=50)
e1.grid(row=2, column=1)
e2 = Entry(root, width=50)
e2.grid(row=3, column=1)
e3 = Entry(root, width=50)
e3.grid(row=4, column=1)
e4 = Entry(root, width=50)
e4.grid(row=5, column=1)

# Create database
# Comment if already created
"""
create_Issuer = ''' CREATE TABLE Issuer (
    Student_Name VARCHAR(255),
    Student_SRN VARCHAR(255),
    Book_Title VARCHAR(255),
    Book_ISBN INT
)'''
isk.execute(create_Issuer)
"""

def getData():
    countIndex = 0
    data = []
    d = bkk.execute('''SELECT * FROM Bookmaster''')
    for l in list(d):
        if e1.get() == l[0] and int(e2.get()) == l[1]:
            countIndex += 2
            break
    D = std.execute('''SELECT * FROM Studentmaster''')
    for k in list(D):
        if e3.get() == k[0] and e4.get() == k[1]:
            countIndex += 2
            break
    if countIndex == 4:
        data.append(e1.get())
        data.append(int(e2.get()))
        data.append(e3.get())
        data.append(e4.get())
        return data

def issueUpdate():
    iss = sqlite3.connect('Issuer.db')
    isk = iss.cursor()
    bk = sqlite3.connect('Bookmaster.db')
    bkk = bk.cursor()
    st = sqlite3.connect('Studentmaster.db')
    std = st.cursor()
    data = getData()
    try:
       if len(data) == 4:
          isk.execute('''INSERT INTO Issuer (Student_Name, Student_SRN, Book_Title, Book_ISBN) VALUES (?,?,?,?)''',(data[0], data[1], data[2], (data[3])))
          bkk.execute('''UPDATE Bookmaster SET Copies_Available = 'Borrowed' WHERE (Book_Title, Book_ISBN) = (?,?)''',(data[0], (data[1])))
          std.execute('''UPDATE Studentmaster SET Books_Borrowed = Books_Borrowed+1 WHERE (Student_Name, Student_SRN) = (?,?)''',(data[2], data[3]))
          iss.commit()
          bk.commit()
          st.commit()
          messagebox.showinfo("Success",'Book Issued.')
       else:
          messagebox.showerror("Error",'Book/Student not in list.')
    except:
        messagebox.showerror("Value Error",'Please enter valid value.')

def returnUpdate():
    iss = sqlite3.connect('Issuer.db')
    isk = iss.cursor()
    re = sqlite3.connect('Return.db')
    ret = re.cursor()
    bk = sqlite3.connect('Bookmaster.db')
    bkk = bk.cursor()
    st = sqlite3.connect('Studentmaster.db')
    std = st.cursor()
    data = getData()
    if len(data) == 4:
        ret.execute('''INSERT INTO Return (Book_Title, Book_ISBN, Student_Name, Student_SRN) VALUES (?,?,?,?)''',(data[0], int(data[1]), data[2], data[3]))
        bkk.execute('''UPDATE Bookmaster SET Copies_Available = 'Available' WHERE (Book_Title, Book_ISBN) = (?,?)''',(data[0], int(data[1])))
        std.execute('''UPDATE Studentmaster SET Books_Borrowed = Books_Borrowed-1 WHERE (Student_Name, Student_SRN) = (?,?)''',(data[2], data[3]))
        isk.execute('''DELETE FROM Issuer WHERE (Book_Title, Book_ISBN, Student_Name, Student_SRN) = (?,?,?,?)''',(data[0], int(data[1]), data[2], data[3]))
        re.commit()
        iss.commit()
        bk.commit()
        st.commit()
        messagebox.showinfo(message='Returned.')
    else:
        messagebox.showerror(message='Book/Student not found.')

ISS = Button(root, text='ISSUE BOOK', padx=12, pady=2, command=issueUpdate).grid(row=7, column=0, columnspan=2)
ISBN = e2.get()
SRN = e4.get()
btn_return = Button(root, text="RETURN BOOK", padx=12, pady=2, command=returnUpdate).grid(row=7, column=1, columnspan=2)
Label(root, text='', width=50).grid(row=8, column=1)

iss.commit()
iss.close()
root.mainloop()