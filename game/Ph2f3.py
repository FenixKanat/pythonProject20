from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as tkfont
import textwrap
import os


class Ph2f3(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        path = "../Assets/Phase2.jpg"
        self.img = ImageTk.PhotoImage(Image.open(os.path.join(self.controller.dirname, path)))

        background_label = Label(self, image=self.img)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        font = tkfont.Font(family="Times New Roman", size=16, weight="bold")

        text = textwrap.fill("Lisa is now in a mental health hospital, trying her best to overcome "
                             "the struggles she went through and the reasons behind them.",
                             width=50)

        text = Label(self, width=50, text=text)
        text.configure(font=font)
        text.place(relx=0.5, rely=0.3, anchor=CENTER)

        btn1_frame2 = Button(self, text="Next", bg='white', fg='black', font=self.controller.font,
                             command=lambda: self.controller.show_frame('Ph3f1'))
        btn1_frame2.place(relx=0.5, rely=0.5, width=150, height=50, anchor=CENTER)
