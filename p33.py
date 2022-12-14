from tkinter import *
root = Tk()

l1 =Label(root,text="Image",justify=LEFT,pady=10)
l1.pack(side=LEFT)

p1 = PhotoImage(file="C:/Users/Lenovo/OneDrive/Pictures/lock.gif")
l2= Label(root,image=p1)
l2.pack(side=RIGHT)

root.mainloop()