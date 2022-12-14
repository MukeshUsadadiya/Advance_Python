# mesaage  Box

from tkinter import *
import tkinter.messagebox
root = Tk()
root.geometry("400x400")
root.resizable(0,0)

def show():
    tkinter.messagebox.showinfo("BCA - 6","MK")
    tkinter.messagebox.showwarning("BCA - 6","MK")
    tkinter.messagebox.showerror("BCA - 6","MK")
    tkinter.messagebox.askquestion("BCA - 6","MK")
    tkinter.messagebox.askokcancel("BCA - 6","MK")
    tkinter.messagebox.askyesno("BCA - 6","MK")
    tkinter.messagebox.askretrycancel("BCA - 6","MK")

b1 = Button(root,text="Click",font=("Airal",20),command=show)

b1.pack()
root.mainloop()