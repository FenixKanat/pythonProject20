from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as tkfont
import textwrap
import os


class Ph1f1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        path = "../Assets/Phase2.jpg"
        self.img = ImageTk.PhotoImage(Image.open(os.path.join(self.controller.dirname, path)))

        background_label = Label(self, image=self.img)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        font = tkfont.Font(family="Times New Roman", size=16, weight="bold")

        text = textwrap.fill("loses job bcz of mental health",
                             width=50)

        text = Label(self, width=50, text=text)
        text.configure(font=font)
        text.place(relx=0.5, rely=0.3, anchor=CENTER)

        btn_option1 = Button(self, text="1- parents ", bg='white', fg='black', font=self.controller.font,
                             command=lambda: self.controller.show_frame('Ph1f2'))
        btn_option1.place(relx=0.5, rely=0.6, width=150, height=50, anchor=CENTER)

        btn_option2 = Button(self, text="2- friends ", bg='white', fg='black', font=self.controller.font,
                             command=lambda: self.controller.show_frame('Ph1f3'))
        btn_option2.place(relx=0.5, rely=0.7, width=150, height=50, anchor=CENTER)