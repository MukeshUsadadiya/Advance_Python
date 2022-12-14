from tkinter import *
root = Tk()
root.geometry("400x400")
root.resizable(0 , 0)
def show():
    print("mk")
    root.configure(background="red")
b1 = Button(root,text="Login",font=("Airal",20),command=show)
b1.config(command=show)
b1.bind("<Button>",show)
b1.pack()
root.mainloop()