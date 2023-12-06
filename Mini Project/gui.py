from tkinter import *
import tkinter.messagebox

root = Tk()

choice = "n"

def Yes():
    choice = "y"
def No():
    choice = "n"
def Clear():
    e1.delete(0, END)
    e2.delete(0, END)
def Submit():
    ISBN = e1.get()
    SRN = e2.get()
    tkinter.messagebox.showinfo("Success", "Book Issued.")
def Exit():
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