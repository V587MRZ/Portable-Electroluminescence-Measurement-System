"""GUI for Portable EL System v2.0"""
# Editor: Yixin Lu
# Date:  March 26


from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import webbrowser

from picamera import PiCamera
import time
import numpy as np
import cv2


# Create a application masters from the main window
class Application(Frame):
    # initialize the application area
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        # Create the Project Label
        self.label01 = Label(self, text="Portable Electroluminescence \n"
                             "Measurement System", fg="Black",
                             font=("Times", 20, "bold italic"))

        # Create the ANU Label
        global photo_ANU
        photo_ANU = Image.open("ANU_Label.gif")
        photo_ANU = ImageTk.PhotoImage(photo_ANU.resize((186, 80)))
        self.label02 = Label(self, height=80, image=photo_ANU)

        global photo01
        photo01 = Image.open("image1.jpg")
        photo01 = ImageTk.PhotoImage(photo01.resize((500, 300)))

        global photo02
        photo02 = Image.open("image2.jpg")
        photo02 = ImageTk.PhotoImage(photo02.resize((500, 300)))

        global photo_diff
        photo_diff = Image.open("diff.jpg")
        photo_diff = ImageTk.PhotoImage(photo_diff.resize((500, 300)))

        # Create a notebook for picture results
        self.pictures = ttk.Notebook(self)
        s = ttk.Style()
        s.configure('TNotebook', tabposition='en')
        s.configure('TNotebook.Tab', padding=(7,41))
        self.frame01 = ttk.Frame(self.pictures, width=500, height=300)
        self.frame02 = ttk.Frame(self.pictures, width=500, height=300)
        self.frame03 = ttk.Frame(self.pictures, width=500, height=300)
        self.pictures.add(self.frame01, text="Image1")
        self.pictures.add(self.frame02, text="Image2")
        self.pictures.add(self.frame03, text="Image3")
        ttk.Label(self.frame01, image=photo01).grid(column=3, row=3)
        ttk.Label(self.frame02, image=photo02).grid(column=3, row=3)
        ttk.Label(self.frame03, image=photo_diff).grid(column=3, row=3)

        # Create the team member list
        self.btnMember = Button(self, text="Team Members", width=26,
                                command=self.Members_list)

        # Create the start button
        self.btnStart = Button(self, text="Start Testing", width=26, command=self.Start)

        # Create a button linking to the Project Landing Page
        self.btnLPage = Button(self, text="Project Landing Page", width=26)
        self.btnLPage.bind("<1>", self.LandingPage)

        # Create a button linking to the repository
        self.btnRPage = Button(self, text="Project Repository", width=26)
        self.btnRPage.bind("<1>", self.RepositoryPage)

        # Create the exit button
        self.btnQuit = Button(self, text="Quit", width=26,
                              command=root.destroy)

        # Use Grid Geometry Manager to place widgets
        self.label01.grid(column=1, row=0, columnspan=5, rowspan=1)
        self.label02.grid(column=0, row=0)
        self.pictures.grid(column=0, row=1, columnspan=4, rowspan=5, pady=10,
                           sticky=W)
        self.btnLPage.grid(column=5, row=1)
        self.btnRPage.grid(column=5, row=2)
        self.btnStart.grid(column=5, row=3)
        self.btnMember.grid(column=5, row=4)
        self.btnQuit.grid(column=5, row=5, sticky=S)

    def Members_list(self):
        newWindow = Toplevel(root)
        newWindow.title("Team Infomation")
        newWindow.geometry("500x300")
        Label(newWindow, text="Team Members",
              font=("Times", 20, "bold")).grid(row=0, column=0, pady=10)
        Label(newWindow,
              text="Project Mentors: ").grid(row=1, column=0, pady=0, sticky=W)

    def Start(self):
        self.camera = PiCamera()

        self.camera.capture('/home/portableel/image1.jpg')
        print("first pic being taken")
        time.sleep(5)
        self.camera.capture('/home/portableel/image2.jpg')
        print("second pic being taken")

        img1 = cv2.imread('/home/portableel/image1.jpg',cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread('/home/portableel/image2.jpg',cv2.IMREAD_GRAYSCALE)
        diff = cv2.absdiff(img1,img2)
        cv2.imwrite('/home/portableel/diff.jpg',diff)
        time.sleep(2)
        self.camera.close()

        global photo01
        photo01 = Image.open("image1.jpg")
        photo01 = ImageTk.PhotoImage(photo01.resize((500, 300)))

        global photo02
        photo02 = Image.open("image2.jpg")
        photo02 = ImageTk.PhotoImage(photo02.resize((500, 300)))

        global photo_diff
        photo_diff = Image.open("diff.jpg")
        photo_diff = ImageTk.PhotoImage(photo_diff.resize((500, 300)))

        ttk.Label(self.frame01, image=photo01).grid(column=3, row=3)
        ttk.Label(self.frame02, image=photo02).grid(column=3, row=3)
        ttk.Label(self.frame03, image=photo_diff).grid(column=3, row=3)

    def LandingPage(self, event):
        webbrowser.open("https://u6283651.wixsite.com/luminescent")

    def RepositoryPage(self, event):
        webbrowser.open("https://anu365.sharepoint.com"
                        "/sites/PortableELdeviceProject")


if __name__ == "__main__":
    # Creating the Tkinter Window
    root = Tk()
    # Custumise the main window of the GUI
    root.title("Portable Electroluminescence Measurement System")
    # root.geometry("800x400")
    root.attributes('-fullscreen', True)
    app = Application(master=root)  # reset the master of the application
    root.mainloop()
