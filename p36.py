import tkinter as tk
count =0
def count_label(l1):
    def c1():
        global count
        count = count + 1
        l1.config(text=str(count))
        l1.after(1000,c1)
    c1()
def s1():
    l1.config(text ="0")
root = tk.Tk()
root.title("Counting Seconds")
l1 = tk.Label(root,fg="green")
l1.pack()
count_label(l1)
b1= tk.Button(root,text="Start",width=25,command=s1)
b1.pack()
b2 = tk.Button(root,text="End",width=25,command=root.destroy)
b2.pack()
root.mainloop()