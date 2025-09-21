from tkinter import *
root.title = Tk(yarmouk)
v = IntVar(5)
Radiobutton(root, text='GfG', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='MIT', variable=v, value=2).pack(anchor=W)
mainloop()