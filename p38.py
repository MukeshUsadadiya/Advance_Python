from tkinter import *
root = Tk()
root.geometry("400x400")
root.resizable(0,0)
l1 = Label(root,text="A List of Subjects....")
lb1 = Listbox(root)
lb1.insert(1, "Python")
lb1.insert(2, "DWDM")
lb1.insert(3, "Android")
lb1.insert(4, "Project")
lb1.insert(5, "Practical")
b1 = Button(root, text="Delete", command=lambda lb1= lb1 : lb1.delete(ANCHOR))
l1.pack()
lb1.pack()
b1.pack()
mainloop()