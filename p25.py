
#create a star using polugon and canvas class

from tkinter import *
root = Tk()
root.geometry("400x400")
root.resizable(0,0)

c = Canvas(root,height=250,width=300)
p1=[100,10,40,198,198,78,10,78,160,198]

o = c.create_polygon(p1,fill="green",outline="red")
c.pack()
root.mainloop()