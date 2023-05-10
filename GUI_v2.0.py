"""GUI for Portable EL System v2.0"""
# Editor: Yixin Lu
# Date:  April 19


from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk

import picamera 
import time
import numpy as np
import cv2
import RPi.GPIO as GPIO

from Camera import capture_and_diff


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
        self.label01 = Label(self, text="Portable Electroluminescence "
                             "Measurement System", fg="Black",
                             font=("Times", 20, "bold italic"))

        # Use option menu to select the Operation Mode
        self.OperationMode = StringVar(self)
        self.OperationMode.set("Auto")
        self.OptM = OptionMenu(self, self.OperationMode,"    Auto    ", "    Manual    ",
                               command=self.Entry_able)

        # Create the entry area for number of samples, iso, and resolution
        self.pairs = StringVar(self)
        self.pairs.set("50")
        self.entry_pairs = Entry(self, width=15, textvariable=self.pairs)

        self.iso = StringVar(self)
        self.iso.set("800")
        self.entry_iso = Entry(self, width=15, textvariable=self.iso)

        self.resolution = StringVar(self)
        self.resolution.set("(512,512)")
        self.entry_resolution = Entry(self, width=15, textvariable=self.resolution)

        self.entry_iso.config(state="disabled")
        self.entry_pairs.config(state="disabled")
        self.entry_resolution.config(state="disabled")

        global photo_diff
        photo_diff = Image.open("average_diff_image.jpg")
        photo_diff = ImageTk.PhotoImage(photo_diff.resize((500, 300)))
        self.label02 = Label(self, image=photo_diff)

        # Create the start button
        self.btnStart = Button(self, text="Start Testing",height=2,
                               font=(10), width=26, command=self.Start)

        # Create the exit button
        self.btnQuit = Button(self, text="Quit", height=2, width=26,
                              font=(10),command=root.destroy)\
                              
        self.camera = Button(self, text="Test Camera", height=2, width=26,
                              font=(10),command=self.camera_preview)

        # Use Grid Geometry Manager to place widgets
        self.label01.grid(column=0,row=0,columnspan=3,pady=40)
        self.btnStart.grid(column=2,row=5,columnspan=2,pady=20)
        self.camera.grid(column=2,row=6,columnspan=2)
        self.btnQuit.grid(column=2,row=7,columnspan=2,sticky=N)
        self.OptM.grid(column=3,row=1,columnspan=2)
        Label(self, text="Operation Mode: ").grid(column=2,row=1,sticky=W,pady=20)
        self.entry_pairs.grid(column=3,row=2)
        Label(self, text="Pairs of Images: ").grid(column=2,row=2,sticky=W)
        self.entry_iso.grid(column=3,row=3)
        Label(self, text="Camera Iso: ",).grid(column=2,row=3,sticky=W)
        self.entry_resolution.grid(column=3,row=4)
        Label(self, text="Camera Resolution: ").grid(column=2,row=4,sticky=W)
        self.label02.grid(column=0, row=1,columnspan=2,rowspan=6,stick=S, pady=20)

        Label(self, text="Created by: Yixin Lu, Levi Zhang"
              ", Zhengdao Zhou, Bhargav Ashok, Balaji R, Andrew Leong",
              fg="Grey", font=("Times", 8)).grid(column=0,row=7,sticky=W)
        
        self.rowconfigure(7,weight=1)


    def Entry_able(self,root):
        if self.OperationMode.get() == "    Auto    ":
            self.entry_iso.config(state="disabled")
            self.entry_pairs.config(state="disabled")
            self.entry_resolution.config(state="disabled")

        if self.OperationMode.get() == "    Manual    ":
            self.entry_iso.config(state="normal")
            self.entry_pairs.config(state="normal")
            self.entry_resolution.config(state="normal")

    def Start(self):
        global photo_diff
        if self.OperationMode.get() == "Auto":
            capture_and_diff()
        else:
            capture_and_diff(num_photos=int(self.entry_pairs.get()), 
                                iso=int(self.entry_iso.get()), 
                                resolution=eval(self.entry_resolution.get()))
        photo_diff = Image.open("average_diff_image.jpg")
        photo_diff = ImageTk.PhotoImage(photo_diff.resize((500, 300)))
        self.label02["image"]=photo_diff
        self.label02.grid(column=0, row=1,columnspan=2,rowspan=6,pady=20)
    
    def camera_preview(self):
        with picamera.PiCamera() as camera:
            # 设置预览分辨率
            camera.resolution = (500, 300)
            # 打开预览
            camera.start_preview(fullscreen=False, window=(7,130,500,300))
            # 延时
            time.sleep(5)
            # 关闭预览
            camera.stop_preview()
            


if __name__ == "__main__":
    # Creating the Tkinter Window
    root = Tk()
    # Custumise the main window of the GUI
    root.title("Portable Electroluminescence Measurement System")
    # root.geometry("800x400")
    root.attributes('-fullscreen', True)
    app = Application(master=root)  # reset the master of the application
    root.mainloop()
