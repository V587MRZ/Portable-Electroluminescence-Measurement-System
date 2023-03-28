"""Learning Practices 06"""
# 06: The Grid Geometry Manager
# Date:  March 16


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
        # Create a label
        self.label01 = Label(self, text="Username")

        # Use grid geometry manager to place the label in row and column
        self.label01.grid(row=0, column=0)

        # Placing more widgets by using grid method
        self.entry01 = Entry(self)
        self.entry01.grid(row=0, column=1)

        # To create a widget quickly, we could use this method
        # However, the certain widget could bot be changed after it is created
        Label(self, text="Username is the team name").grid(row=0, column=2)
        Label(self, text="Password").grid(row=1, column=0)
        Entry(self, show="*").grid(row=1, column=1)

        # "sticky" could be used to change the layout within the cell
        Button(self, text="Login").grid(row=2, column=1, sticky=EW)
        Button(self, text="Cancel").grid(row=2, column=2, sticky=E)


if __name__ == "__main__":
    # Creating the Tkinter Window
    root = Tk()
    # Custumise the main window of the GUI
    root.title("Portable EL")
    root.geometry("500x300+100+200")  # size and position of the window

    app = Application(master=root)  # reset the master of the application
    root.mainloop()
