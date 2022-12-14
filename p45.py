#Message
from tkinter import *
root = Tk()
root.geometry("400x400")
root.resizable(0,0)
str = "This is a Message. This display data tabular format automatically"
msg = Message(root,text=str)
msg.config(bg="pink",font=("Times",23,"italic"))
msg.pack()
mainloop()