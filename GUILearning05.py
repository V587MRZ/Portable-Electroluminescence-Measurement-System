"""Learning Practices 05"""
# 05: Entry & StringVar
# Date:  March 6


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
        self.label01 = Label(self, text="user name")
        self.label01.pack()

        # StringVar is linked to the Entry widget
        # StringVar changes with the change of the Entry widget
        # Entry widget changes with the change of the StringVar
        v1 = StringVar()
        self.entry01 = Entry(self, textvariable=v1)
        self.entry01.pack()
        # set a value to the StringVar
        v1.set("Portable EL")

        # create a password input window
        self.label02 = Label(self, text="password")
        self.label02.pack()
        v2 = StringVar()
        self.entry02 = Entry(self, textvariable=v2, show="*")
        self.entry02.pack()

        self.btn01 = Button(self, text="Log in", command=self.login)
        self.btn01.pack()

    def login(self):
        username = self.entry01.get()
        pwd = self.entry02.get()
        # Tests if the system get the input
        print("user name: "+username)
        print("password: "+pwd)

        if username == "Yixin Lu" and pwd == "123456":
            messagebox.showinfo("Portable EL System", "Success!")
        else:
            messagebox.showinfo("Portable EL System",
                                "Incorrect username or password")


if __name__ == "__main__":
    # Creating the Tkinter Window
    root = Tk()
    # Custumise the main window of the GUI
    root.title("Portable EL")
    root.geometry("1000x600+100+200")  # size and position of the window

    app = Application(master=root)  # reset the master of the application
    root.mainloop()
