import tkinter 
from tkinter import *
from tkinter import messagebox

root = tkinter.Tk()
root.title("Hello")

btn = Checkbutton(root, text="Checkbutton")
btn.pack()
bx = Spinbox(root, from_=0, to=10)
bx.pack()

x = bx.get()


if btn.select():
    messagebox.showinfo("The value is probably",x)

root.mainloop()