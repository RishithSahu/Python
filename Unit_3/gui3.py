#                                         GUI 3
import tkinter
wind = tkinter.Tk()
wind.title("Tkinter Canvas Widget")

canvas = tkinter.Canvas(wind, width=300, height=300, bg="blue")
cord = 10,10,300,300
arc1 = canvas.create_arc(cord, start=0, extent=150, fill="grey")
arc2 = canvas.create_arc(cord, start=150, extent=215, fill="black")
canvas.pack()
wind.mainloop()