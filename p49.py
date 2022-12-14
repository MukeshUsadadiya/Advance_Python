from tkinter import *

def sl1():
    selectors = "Value "+str(var.get())
    l1.config(text=selectors)
root = Tk()
root.geometry("400x400")
root.resizable(0,0)
var = DoubleVar()
s1 = Scale(root, variable=var,from_=10, to=80, orient=HORIZONTAL)
s1.pack()
b1 = Button(root, text="Get Scale Value :",command=sl1)
b1.pack()
l1 = Label(root)
l1.pack()
root.mainloop()
