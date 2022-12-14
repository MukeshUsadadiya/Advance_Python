from tkinter import *
root = Tk()
root.geometry("400x400")
def c1():
    m1 = lb1.get(lb1.curselection())
    l2.config(text="Selected Subject is : "+str(m1))
    l2.grid(column=3,row=0)
root.title("Select The Number from ListBox")
l1 = Label(root, text="Select Value..", font=("Century Schoolbook",15))
l1.grid(column=00,row=0)
lb1 = Listbox(root,selectmode=SINGLE,width=15,height=10,font=("Century Schoolbook",25))
lb1.grid(column=1,row=0)
l2 = Label(root,text="",font=("Century Schoolbook",25))
l = ["Python","DWDM","Android","Project"]
for i in l:
    lb1.insert(END,i)
b1 = Button(root,text="Click Hear",width=25,command=c1)
b1.grid(column=1,row=1)
mainloop()
