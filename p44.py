from tkinter import *
from tkinter.filedialog import *
root = Tk()
root.title("Untitled-Notepad")
def newFile():
    ta.delete(1.0, END)
def Openfile():
    name = askopenfilename()
def Savefile():
    name = asksaveasfile()
def Saveas():
    name= asksaveasfilename()
m1 = Menu(root)
file = Menu(m1, tearoff=0)
file.add_command(label="New",accelerator="Ctlr+N",command=newFile)
file.add_command(label="Open", command=Openfile)
file.add_command(label="Save", command=Savefile)
file.add_command(label="Save As..",command=Saveas)
file.add_separator()
file.add_command(label="Page Setup")
file.add_command(label="Print")
file.add_separator()
file.add_command(label="Close",command=root.quit)
m1.add_cascade(label="File", menu=file)

edit = Menu(m1, tearoff=0)
edit.add_command(label="Undo")
edit.add_separator()
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
edit.add_command(label="Delete")
m1.add_cascade(label="Edit", menu=edit)

help = Menu(m1, tearoff=0)
help.add_command(label="About")
help.add_command(label="Help")
m1.add_cascade(label="Help", menu=help)
ta = Text(root)
ta.pack(expand=True,fill=BOTH)
root.config(menu=m1)
root.mainloop()
