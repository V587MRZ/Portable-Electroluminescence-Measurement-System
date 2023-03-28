"""Learning Practices 04"""
# 04-1: Button
# Date:  March 6

# 04-2: Radiobutton & Checkbutton
# Date:  March 14

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
        # create a button to exit the whole functions
        self.btnQuit = Button(root, text="Quit", command=root.destroy)
        # list all options when creating the Quit button
        self.btnQuit.pack()

        global photo01
        # set the photo01 as the global variable. Since the main program is a
        # continuing loop, it may dispare if not save it as global variable
        photo01 = PhotoImage(file="img/ANU_Label.gif")

        # Button could show image instead of text, the following is an example
        # Create a button that could be used
        self.btn02 = Button(self, image=photo01, command=self.Members_list)
        self.btn02.pack()
        # Button could be controlled to be abled and disabled
        self.btn03 = Button(self, image=photo01, command=self.Members_list)
        self.btn03.pack()
        self.btn03.config(state="disabled")

        # The location of the text on the button could be changed by 'anchor='
        # create another button to exit the whole functions
        self.btnQuit = Button(root, text="Quit02", width=12, height=3,
                              anchor=E, command=root.destroy)
        # list all options when creating the Quit button
        self.btnQuit.pack()

    # 04-2 Radiobutton and Checkbutton:
        # create a veriable to store the name initial
        self.v = StringVar()
        self.v.set("NULL")
        # create three Radiobutton for user to choose from
        # only one button could be choosen and stored in the variable
        self.r1 = Radiobutton(root, text="Yixin Lu", value="YL",
                              variable=self.v)
        self.r2 = Radiobutton(root, text="Zhengdao Zhou", value="ZL",
                              variable=self.v)
        self.r3 = Radiobutton(root, text="Levi Zhang", value="LZ",
                              variable=self.v)
        self.r1.pack(side="left")
        self.r2.pack(side="left")
        self.r3.pack(side="left")

        self.r4 = Button(root, text="Confirm", command=self.confirm)
        self.r4.pack(side="left")

        self.software = IntVar()
        self.hardware = IntVar()
        self.c1 = Checkbutton(root, text="Software Team",
                              variable=self.software, onvalue=1, offvalue=0)
        self.c2 = Checkbutton(root, text="Hardware Team",
                              variable=self.hardware, onvalue=1, offvalue=0)
        self.c3 = Button(root, text="Confirm", command=self.confirm_team)
        self.c3.pack(side="right")
        self.c1.pack(side="right")
        self.c2.pack(side="right")

    def Members_list(self):
        messagebox.showinfo("Members List", "Yixin Lu")

    def confirm(self):
        messagebox.showinfo("Member Selection",
                            "Name Initial: " + self.v.get())

    def confirm_team(self):
        if self.software.get() == 1:
            messagebox.showinfo("Subteams",
                                "Your sub-team is software")
        if self.hardware.get() == 1:
            messagebox.showinfo("Subteams",
                                "Your sub-team is hardware")
        if self.hardware.get() == 0 and self.software.get() == 0:
            messagebox.showinfo("Subteams",
                                "Please make an selection.")


if __name__ == "__main__":
    # Creating the Tkinter Window
    root = Tk()
    # Custumise the main window of the GUI
    root.title("Portable EL")
    root.geometry("1000x600+100+200")  # size and position of the window

    app = Application(master=root)  # reset the master of the application
    root.mainloop()
