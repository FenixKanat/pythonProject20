from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as tkfont
import textwrap
import os


class Ph2f2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        path = "../Assets/Phase2.jpg"
        self.img = ImageTk.PhotoImage(Image.open(os.path.join(self.controller.dirname, path)))

        background_label = Label(self, image=self.img)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        font = tkfont.Font(family="Times New Roman", size=16, weight="bold")

        text = textwrap.fill("Before moving out, Lisa has tried to seek a shelter for few days with no result, "
                             "Lisa has no other option but to submit to a mental health hospital, "
                             "seeking both a shelter and help with her current mental state.",
                             width=50)

        text = Label(self, width=50, text=text)
        text.configure(font=font)
        text.place(relx=0.5, rely=0.3, anchor=CENTER)

        btn1_frame2 = Button(self, text="Next", bg='white', fg='black', font=self.controller.font,
                             command=lambda: self.controller.show_frame('Ph2f3'))
        btn1_frame2.place(relx=0.5, rely=0.5, width=150, height=50, anchor=CENTER)
