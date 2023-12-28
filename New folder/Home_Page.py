from tkinter import *
from tkinter import ttk

class LIB_M_SYS:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.state('zoomed')

        lbltitle=Label(self.root,text="Library Management System",bg="LightSteelBlue4",fg="purple",bd=12,relief=RIDGE,font=("bauhaus 93",24),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)


        # ============================== DataFrames ===================================

        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="LightSteelBlue4")
        frame.place(x=0, y=72.3, width=1366, height=400)

        DataFrameLeft = LabelFrame(frame, text="Library Membership Info",bg="LightSteelBlue4",fg="purple",bd=12,relief=RIDGE,font=("bauhaus 93",21),padx=2,pady=6) 
        DataFrameLeft.place(x=-9, y=3, width=900, height=365)

        DataFrameRight = LabelFrame(frame, text="Library Book Info",bg="LightSteelBlue4",fg="purple",bd=12,relief=RIDGE,font=("bauhaus 93",21),padx=2,pady=6) 
        DataFrameRight.place(x=900, y=3, width=420, height=365)

        # ============================== Buttons ===================================

        ButtonFrame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="LightSteelBlue4")
        ButtonFrame.place(x=0, y=472.45, width=1366, height=70)

        # ============================== User Details ===================================

        DetailsFrame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="LightSteelBlue4")
        DetailsFrame.place(x=0, y=542.499, width=1366, height=155)

        # Member--------------------------------------------------------------------------------------
        lblMember = Label(DataFrameLeft, text="Member Type",bg="LightSteelBlue4",fg="black",font=("comic sans ms",14))
        lblMember.grid(row=0, column=0, sticky=W)

        Members = ttk.Combobox(DataFrameLeft, font=("comic sans ms",14), width=20, state="readonly")
        Members['values'] = ("Admin", "Faculty", "Student")
        Members.grid(row=0, column=1)
        # Member--------------------------------------------------------------------------------------
        # PRN--------------------------------------------------------------------------------------
        lblPRN = Label(DataFrameLeft, text="Enter PRN :",bg="LightSteelBlue4",fg="black",font=("comic sans ms",14))
        lblPRN.grid(row=1, column=0, sticky=W)

        PRN = Entry(DataFrameLeft, font=("comic sans ms",14), width=21)
        PRN.grid(row=1, column=1)
        # PRN--------------------------------------------------------------------------------------





if __name__ == "__main__":
    root=Tk()
    obj = LIB_M_SYS(root)
    root.mainloop()