"""Learning Practices 03"""
# 03: Label, image as label, label border
# Date: March 2 & March 6


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
                             font=("Times", 20, "bold italic"))
        # bg: Blackground, fg: Frontground
        self.label01.pack()

        # showing an image
        global photo01
        # set the photo01 as the global variable. Since the main program is a
        # continuing loop, it may dispare if not save it as global variable
        photo01 = PhotoImage(file="img/ANU_Label.gif")
        self.label02 = Label(self, image=photo01)
        self.label02.pack()

        # add a label with a border
        self.label04 = Label(self, text="Label border\nchange line",
                             borderwidth=1, relief="solid", justify="right")
        self.label04.pack()


if __name__ == "__main__":
    # Creating the Tkinter Window
    root = Tk()
    # Custumise the main window of the GUI
    root.title("Portable EL")
    root.geometry("1000x600+100+200")  # size and position of the window

    app = Application(master=root)  # reset the master of the application
    root.mainloop()
