#scrollbar
from tkinter import *
root = Tk()
root.geometry("400x400")
root.resizable(0,0)
sb1 = Scrollbar(root)
sb1.pack(side=RIGHT,fill=Y)
ls = Listbox(root,yscrollcommand=sb1.set)
for i in range(1,101):
    ls.insert(END,i)
ls.pack(side=LEFT,fill=BOTH)
sb1.config(command=ls.yview)
root.mainloop()