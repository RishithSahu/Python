#                                GRAPHICAL USER INTERFACE
'''
   import tkinter 
   root = tkinter.Tk()
   root.mainloop()
'''
import tkinter
from tkinter import *
wind = Tk()
wind.title("First tkinter program")
wind.geometry("800x600")
b = Button(wind, text = "Submit")
b.grid(row=0,column=3)
redbutton = Button(wind, text="Blue",fg = "blue")
redbutton.grid(row=0 , column=1)
name = Label(wind , text="Name").grid(row=0,column=0)
wind.mainloop()