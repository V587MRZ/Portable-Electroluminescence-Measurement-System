from tkinter import *
from tkinter import messagebox

root = Tk()

btn01 = Button(root)
btn01["text"] = "Portable EL Members"
btn01.pack()

def members_name(e):
    messagebox.showinfo("Members","Yixin Lu")

btn01.bind("<Button-1>",members_name)

root.mainloop()

