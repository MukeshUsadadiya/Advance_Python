from tkinter import *
root = Tk()
root.geometry("400x400")
root.resizable(0,0)

ch1 = IntVar()
ch2 = IntVar()
ch3 = IntVar()

def set():
    if(ch1.get()==1):
        l.config(text ="Python")
    elif(ch2.get()==1):
        l.config(text ="Android")
    elif(ch3.get()==1):
        l.config(text ="DWDM")
    else:
        l.config(text="No Selected")

l =Label(root,bg="white",width=20,text="Empty")
l.pack()

c1 =  Checkbutton(root,text="python",onvalue=1,offvalue=0,variable=ch1,command=set)
c1.pack()
c2 =  Checkbutton(root,text="Android",onvalue=1,offvalue=0,variable=ch2,command=set)
c2.pack()
c3 =  Checkbutton(root,text="DWDM",onvalue=1,offvalue=0,variable=ch3,command=set)
c3.pack()
root.mainloop()