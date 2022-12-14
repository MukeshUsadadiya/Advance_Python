#canvas

from tkinter import *
root = Tk()
root.geometry("400x400")
root.resizable(0,0)

c = Canvas(root,height=250,width=300)
line = c.create_line(100,50,100,150)

c.pack()
root.mainloop()