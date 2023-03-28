"""Learning Practices 06"""
# 06: Text & Tag Control
# Date:  March 14


from tkinter import *
from tkinter import messagebox
import webbrowser


# Create a application masters from the main window
class Application(Frame):
    # initialize the application area
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        # Create a Text window with size indicated
        self.w1 = Text(root, width=60, height=12, bg="white")
        self.w1.pack()

        # Use "insert" to add text to the window
        # it will insert text at the (row, column),
        # if there is no text in the front, the text will indent forward
        self.w1.insert(1.0, "The Solar Panel X-ray\n\n")
        self.w1.insert(3.3, "An object is luminescent if it emits "
                       "light not caused by heat. The phenomenon of "
                       "Electroluminescence occurs when the flow of electrons "
                       "in certain materials produces heatless light. The "
                       "photoemissionis then captured using an infrared camera"
                       ". The images enable insight into internal damages such"
                       " as micro-cracks and defects, "
                       "similar to an X-ray for a person.")

        # Create several buttons to show how to modify the text
        self.btn01 = Button(self, text="re-enter text",
                            command=self.insertText)
        self.btn01.pack(side="left")

        self.btn02 = Button(self, text="return text", command=self.returnText)
        self.btn02.pack(side="left")

        self.btn03 = Button(self, text="add image", command=self.addImage)
        self.btn03.pack(side="left")

        self.btn04 = Button(self, text="add widget", command=self.addWidget)
        self.btn04.pack(side="left")

        self.btn05 = Button(self, text="'tag' control", command=self.testTag)
        self.btn05.pack(side="left")

    def insertText(self):
        # insert at the cursor
        self.w1.insert(INSERT, '  (cursor)  ')
        # insert at the text end
        self.w1.insert(END, '   (end)  ')

    def returnText(self):
        # return the text from the specific location
        print("Location text: \n"+self.w1.get(1.2, 1.6))
        # return all the text
        print("All text: \n"+self.w1.get(1.0, END))

    def addImage(self):
        self.photo01 = PhotoImage(file="img/ANU_Label.gif")
        self.w1.image_create(END, image=self.photo01)

    def addWidget(self):
        b1 = Button(self.w1, text="Added Button")
        # create a widget in text window
        self.w1.window_create(INSERT, window=b1)

    def testTag(self):
        # select the text according to the position and add tag
        self.w1.tag_add("Label 1 ", 1.0, 1.28)
        # change the tag config
        self.w1.tag_config("Label 1 ", underline=True,
                           font=("Times", 20, "bold italic"))
        # bing the tag with an event
        self.w1.tag_bind("Label 1 ", "<Button-1>", self.webshow)

    def webshow(self, event):
        # use webbrowser to open a website
        webbrowser.open("https://u6283651.wixsite.com/luminescent")


if __name__ == "__main__":
    # Creating the Tkinter Window
    root = Tk()
    # Custumise the main window of the GUI
    root.title("Portable EL")
    root.geometry("500x300+100+200")  # size and position of the window

    app = Application(master=root)  # reset the master of the application
    root.mainloop()
