"""Audit 01"""


# importing functions needed
from tkinter import *
from tkinter import messagebox


# Create a application masters from the main window
class Application(Frame):
    # initialize the application area
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        # create a label
        self.label01 = Label(self, text="Portable EL System", width=500,
                             height=4, bg="white", fg="Black",
                             font=("Times", 30, "bold italic"))
        self.label01.pack()

        # create a button that display the group members
        self.btn01 = Button(self)
        self.btn01["text"] = "Members"
        self.btn01["command"] = self.Members_list
        self.btn01.pack()

        # create a button that runs the whole process
        self.btn02 = Button(self, text="Start", command=self.Run)
        self.btn02.pack()

        # create a button that enters debugging
        self.btn03 = Button(self, text="Debug", command=self.Debug)
        self.btn03.pack()

        # create a button to exit the whole functions
        self.btnQuit = Button(self, text="Quit", command=root.destroy)
        self.btnQuit.pack()

    # create a popup message box
    def Members_list(self):
        messagebox.showinfo("Members List", "Yixin Lu")

    def Run(self):
        messagebox.showinfo("Results", "Developing")

    def Debug(self):
        messagebox.showinfo("Debuger", "Developing")


if __name__ == "__main__":
    # Creating the Tkinter Window
    root = Tk()
    # Custumise the main window of the GUI
    root.title("Portable EL")
    root.geometry("500x300+100+200")  # size and position of the window

    app = Application(master=root)  # reset the master of the application
    root.mainloop()
