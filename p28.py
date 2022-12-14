# Create a arc  using Canvas class

from tkinter import *
root = Tk()
root.geometry("400x400")
root.resizable(0,0)

c = Canvas(root,width=400,height=400)
c.create_arc(20,20,100,100,start=0,extent=180)

c.pack()
root.mainloop()