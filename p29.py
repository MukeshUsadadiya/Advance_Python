# display image

from tkinter import *
root = Tk()
root.geometry("400x400")
root.resizable(0,0)

c = Canvas(root,width=400,height=400)
filename = PhotoImage(file="C:/Users/Lenovo/OneDrive/Pictures/lock.gif")
i =c.create_image(100,100,image=filename)
c.pack()
root.mainloop()