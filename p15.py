from tkinter import *
root = Tk()
root.geometry("400x400")
root.resizable(0,0)
l1= Label(root,text="Enter User Name :")
l1.pack()
e1= Entry(root,font=("Airal",20),fg="blue",bg="pink",width="10")
e1.pack()
root.mainloop()