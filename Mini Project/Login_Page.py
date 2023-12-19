import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

def validate_login():
    # Get the username and password from the input fields.
    username = username_entry.get()
    password = password_entry.get()
        
    global choice
        
    # Check if the username and password are correct.
    if username == "admin" and password == "admin":
        choice = "H"
        root.destroy()
    else:
        # Login failed.
        messagebox.showerror(message="Invalid username or password.")

root = tk.Tk()
root.title("LIBDAT - Login Page")
root.resizable(False, False)
root.configure(background='black')
width = 640
height = 380
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

Label(root, text='LOGIN', font=('Helvetica', 18, 'bold'), bg='black', fg='white').grid(row=0, column=1)

username_entry = tk.Entry(root, width=50, font=('Helvetica', 10, 'bold'))
password_entry = tk.Entry(root, show="*", width=50, font=('Helvetica', 10, 'bold'))

login_button = tk.Button(root, text="Login", command=validate_login, bg='light green', fg='black', font=('Helvetica', 18, 'bold'))
root.bind('<Return>',lambda event : validate_login())

username_entry.grid(row=3, column=1)
logo = ImageTk.PhotoImage(Image.open("D:\Rishith\Python\Mini Project\logo.jpg"))
tk.Label(root, image=logo).grid(row=1, column=1)
tk.Label(root, text='       ', width=20, bg='black').grid(row=2, column=2)
tk.Label(root, text='       ', width=20, bg='black').grid(row=3, column=2)
tk.Label(root, text='Username', font=('Helvetica', 10, 'bold'), width=20, bg='black', fg='white').grid(row=3, column=0)
tk.Label(root, text='Password', font=('Helvetica', 10, 'bold'), width=20, bg='black', fg='white').grid(row=4, column=0)
password_entry.grid(row=4, column=1)
login_button.grid(row=6, column=1)

root.mainloop()

if choice == "H": 
    from Home_Page import *

root.mainloop()