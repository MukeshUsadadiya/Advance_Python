# Create a oval  using Canvas class

from tkinter import *
root = Tk()
root.geometry("400x400")
root.resizable(0,0)

c = Canvas(root,width=400,height=400)
c.create_oval(20,20,100,100)

c.pack()
root.mainloop()