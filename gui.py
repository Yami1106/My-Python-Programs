from tkinter import *
from tkinter import messagebox
a=Tk()
a.geometry("200x200")
def sub():
    msg=messagebox.showinfo("GUI event demo","try")
a.title("Abc")
l1=Label(a,text="name")
l1.grid(row=0)
e1=Entry(a)
e1.grid(column=1)
Button(a,text="submit",width=5,command=sub).grid(row=2)
a.mainloop()
