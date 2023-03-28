"""Learning Practices 01"""
# 01: Main Loop and message box
# Date: Febuary 25
# testing on the raspberry pi


# importing functions needed
from tkinter import *
from tkinter import messagebox


# Creating the Tkinter Window
root = Tk()

# Custumise the main window of the GUI
root.title("Portable EL")
root.geometry("500x300+100+200")
# "wxh+x+y", w is width, h is height,
# x and y are the position of the window

# Create the Button to the members list
btn01 = Button(root)
btn01["text"] = "Members"
# change the text on the button 
btn01.pack()
# use the automatic packing to display the button in GUI


def Members_list(e):
    messagebox.showinfo("Members List", "Yixin Lu")


btn01.bind ("<Button-1>", Members_list)
root.mainloop()
