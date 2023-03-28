"""Learning Practices 02"""
# 02: Application, creatWidget, destory
# Date: March 2


from tkinter import *
from tkinter import messagebox


# Create a application masters from the main window
class Application(Frame):
    # initialize the application area (could be using as a template)
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        # create a button that display the group members
        self.btn01 = Button(self)
        self.btn01["text"] = "Members"
        # change the text on the button 
        self.btn01["command"] = self.Members_list
        # link the button01 with the members list message box
        self.btn01.pack()

        # create a button to exit the whole functions
        self.btnQuit = Button(self, text="Quit", command=root.destroy)
        # list all options when creating the Quit button
        self.btnQuit.pack()

    # create a popup message box
    def Members_list(self):
        messagebox.showinfo("Members List", "Yixin Lu")


if __name__ == "__main__":
    # Creating the Tkinter Window
    root = Tk()
    # Custumise the main window of the GUI
    root.title("Portable EL")
    root.geometry("500x300+100+200")  # size and position of the window

    # the following could be used as template
    app = Application(master=root)  # reset the master of the application
    root.mainloop()
