from tkinter import *
root = Tk()
m1 = Menu(root)
file = Menu(m1,tearoff=0)
file.add_command(label="New",accelerator="Ctrl+N")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save As...")
file.add_separator()
file.add_command(label="Page Setup")
file.add_command(label="Print")
file.add_separator()
file.add_command(label="Colse",command=root.quit)
m1.add_cascade(label="File",menu=file)

edit = Menu(m1,tearoff=0)
edit.add_command(label="Undo")
edit.add_separator()
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
edit.add_command(label="Delete")
m1.add_cascade(label="Edit",menu=edit)

help = Menu(m1,tearoff=0)
help.add_command(label="About")
help.add_command(label="Help")
m1.add_cascade(label="Help",menu=help)

root.config(menu=m1)
root.mainloop()