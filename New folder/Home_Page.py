from tkinter import *

class LIB_M_SYS:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.state('zoomed')




        lbltitle=Label(self.root,text="Library Management System",bg="LightSteelBlue4",fg="purple",bd=20,relief=RIDGE,font=("bauhaus 93",49 ,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)




if __name__ == "__main__":
    root=Tk()
    obj = LIB_M_SYS(root)
    root.mainloop()