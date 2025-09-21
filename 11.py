from tkinter import *
master = Tk()
w = Scale(master, from_=50, to=500)
w.pack()
w = Scale(master, from_=60, to=200, orient=HORIZONTAL)
w.pack()
mainloop()