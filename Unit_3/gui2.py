#                                       GUI 2

from tkinter import *
from tkinter import messagebox 
top = Tk() 
top.geometry("400x250")
name = Label(top, text = "Name").place(x= 30,y = 50)
email = Label(top, text = "Email").place(x= 30,y = 90)
password = Label(top, text="Password").place(x= 30,y = 130)
e1 = Entry(top).place(x= 80,y = 50)
e2 = Entry(top).place(x= 80,y = 90)
e3 = Entry(top).place(x= 95,y = 130)
def fun():
    messagebox.showinfo("Hello","Bruh.")
def fun1():
    messagebox.showinfo("Hello","Not yet implemented for ya.")

bluebutton = Button(top, text="Blue",command=fun ,fg = "blue")
bluebutton.grid(row=0 , column=1)

redbutton = Button(top, text="Red",command=fun ,fg = "red")
redbutton.grid(row=0 , column=2)

b = Button(top, text = "Submit", command=fun1)
b.grid(row=0,column=3)
top.mainloop()