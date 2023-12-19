import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

root = tkinter.Tk()
root.title("LIBDAT - Home Page")
root.resizable(False, False)
root.configure(background='black')
width = 540
height = 295
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

choice = "N"
def database():
     global choice
     choice = "D"
def issue():
     global choice
     choice = "I"

logo = ImageTk.PhotoImage(Image.open("D:\Rishith\Python\Mini Project\logo.jpg"))
Label(root, image=logo).grid(row=1, column=1)
Label(root, text='LIBDAT', font=('Centaur', 25, 'bold'), bg='black', fg='white').grid(row=0, column=1)
b1 = Button(root, text="Issue or Return Books", bg='powder blue', fg='black',font=('Helvetica', 10, 'bold'), padx=5, pady=10, command=lambda: (issue(), root.destroy())).grid(row=2, column=0)
b2 = Button(root, text="Update Library Database", bg='light green', fg='black',font=('Helvetica', 10, 'bold'), padx=5, pady=10, command=lambda : (database(),root.destroy())).grid(row=2, column=2)
root.mainloop()

if choice == "I": 
    from Library_Issuer import *
elif choice == "D":
    from Library_Database_Graphics import *
root.mainloop()