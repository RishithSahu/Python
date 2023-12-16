import tkinter
from tkinter import *
from tkinter import font

root = tkinter.Tk()
root.state('zoomed')
root.title("Library Management System - Home Page")
root.resizable(False, False)
root.geometry("300x200")
root.configure(background="black")

choice = "N"
def database():
     global choice
     choice = "D"
def issue():
     global choice
     choice = "I"

buttonFont = font.Font(family='Helvetica', size=13, weight='bold')

b1 = Button(root, text="Issue or Return Books", width=300, height=18, bg="white", fg="black",font=buttonFont, command=lambda: (issue(), root.destroy())).pack()
b2 = Button(root, text="Update Library Database", width=300, height=20, bg="white", fg="black",font=buttonFont, command=lambda : (database(),root.destroy())).pack()
root.mainloop()

if choice == "I": 
    from Library_Issuer import *
elif choice == "D":
    from Library_Database_Graphics import *
root.mainloop()