"""GUI for Portable EL System v1.0"""
# Editor: Yixin Lu
# Date:  March 17


from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser

# from picamera import PiCamera
from time import sleep
import numpy as np
# import cv2


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
                             font=("Times", 30, "bold italic"))

        # Create the ANU Label
        global photo_ANU
        photo_ANU = PhotoImage(file="img/ANU_Label.gif")
        self.label02 = Label(self, height=120, image=photo_ANU)

        global photo01
        photo01 = Image.open("Camera_code/image01.gif")
        photo01 = ImageTk.PhotoImage(photo01.resize((600, 400)))

        global photo02
        photo02 = Image.open("Camera_code/image02.gif")
        photo02 = ImageTk.PhotoImage(photo02.resize((600, 400)))

        global photo_diff
        photo_diff = Image.open("Camera_code/diff.gif")
        photo_diff = ImageTk.PhotoImage(photo_diff.resize((600, 400)))

        # Create a notebook for picture results
        self.pictures = ttk.Notebook(self)
        self.frame01 = ttk.Frame(self.pictures, width=600, height=400)
        self.frame02 = ttk.Frame(self.pictures, width=600, height=400)
        self.frame03 = ttk.Frame(self.pictures, width=600, height=400)
        self.pictures.add(self.frame01, text="Bright")
        self.pictures.add(self.frame02, text="Dark")
        self.pictures.add(self.frame03, text="Result")
        ttk.Label(self.frame01, image=photo01).grid(column=3, row=3)
        ttk.Label(self.frame02, image=photo02).grid(column=3, row=3)
        ttk.Label(self.frame03, image=photo_diff).grid(column=3, row=3)

        # Create the team member list
        self.btnMember = Button(self, text="Team Members",
                                command=self.Members_list)

        # Create the start button
        self.btnStart = Button(self, text="Start Testing", command=self.Start)

        # Create a button linking to the Project Landing Page
        self.btnLPage = Button(self, text="Project Landing Page")
        self.btnLPage.bind("<1>", self.LandingPage)

        # Create a button linking to the repository
        self.btnRPage = Button(self, text="Project Repository")
        self.btnRPage.bind("<1>", self.RepositoryPage)

        # Create the exit button
        self.btnQuit = Button(self, text="Quit", width=30,
                              command=root.destroy)

        # Use Grid Geometry Manager to place widgets
        self.label01.grid(column=1, row=0, columnspan=5, rowspan=1)
        self.label02.grid(column=0, row=0, sticky=W)
        self.pictures.grid(column=0, row=1, columnspan=4, rowspan=5, pady=20,
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
        self.camera.resolution = (512, 512)
        width, height = self.camera.resolution
        for i in range(5):
            prev_image = np.empty((height, width, 3), dtype=np.uint8)
            # 捕获第一张图像 capture the first img
            self.camera.capture(prev_image, format='bgr')
            gray1 = cv2.cvtColor(prev_image, cv2.COLOR_BGR2GRAY)
            # 等待10秒钟 wait for 10s
            sleep(10)
            current_image = np.empty((height, width, 3), dtype=np.uint8)
            # 捕获第二张图像 capture the second img
            self.camera.capture(current_image, format='bgr')
            gray2 = cv2.cvtColor(current_image, cv2.COLOR_BGR2GRAY)

            # 计算两个图像的差异 diffenet img
            diff_image = cv2.absdiff(gray1, gray2)
            photo_diff = diff_image
            cv2.waitKey(1000)

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
    root.geometry("1000x600+100+100")  # size and position of the window

    app = Application(master=root)  # reset the master of the application
    root.mainloop()
