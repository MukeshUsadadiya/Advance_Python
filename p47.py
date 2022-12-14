#Radio Button
from tkinter import *
root = Tk()
root.geometry("400x400")
root.resizable(0,0)
def sel1():
    root.config(bg="red")
def sel2():
    root.config(bg="blue")
def sel3():
    root.config(bg="green")

r1 = Radiobutton(root,text="Red",value="Python",command=sel1)
r1.select()
r1.pack()
r2 = Radiobutton(root,text="Blue",value="DWDM",command=sel2)
r2.deselect()
r2.pack()
r3 = Radiobutton(root,text="Green",value="Android",command=sel3)
r3.deselect()
r3.pack()


mainloop()