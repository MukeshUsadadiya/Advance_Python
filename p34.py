# Frame

from tkinter import *
root = Tk()

for i in ('blue','red','yellow','white','black'):
    Frame(height=20,width=540,bg=i).pack()

mainloop()