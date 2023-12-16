import tkinter
import tkinter as tk

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
            print("Invalid username or password.")

root = tk.Tk()
root.title("Library Management System - Login Page")
root.resizable(False, False)

width = 365
height = 201
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")

login_button = tk.Button(root, text="Login", command=validate_login)
root.bind('<Return>',lambda event : validate_login())

username_entry.grid(row=3, column=1)
tk.Label(root, text='', width=20).grid(row=0, column=0)
tk.Label(root, text='PLEASE LOGIN', width=20).grid(row=1, column=1)
tk.Label(root, text='', width=20).grid(row=2, column=0)
tk.Label(root, text='', width=20).grid(row=5, column=0)
tk.Label(root, text='', width=15).grid(row=2, column=2)
tk.Label(root, text='', width=20).grid(row=7, column=0)
tk.Label(root, text='Username', width=20).grid(row=3, column=0)
tk.Label(root, text='Password', width=20).grid(row=4, column=0)
password_entry.grid(row=4, column=1)
login_button.grid(row=6, column=1)


root.mainloop()

if choice == "H": 
    from Home_Page import *

root.mainloop()