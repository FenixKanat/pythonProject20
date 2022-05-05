from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as tkfont
import textwrap
import os


class Donate(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        path = "../Assets/purplelight.jpeg"
        self.img = ImageTk.PhotoImage(Image.open(os.path.join(self.controller.dirname, path)))

        background_label = Label(self, image=self.img)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        font = tkfont.Font(family="Times New Roman", size=16, weight="bold")

        text = textwrap.fill('we thank you for playing our game there are a lot of homless people '
                             'who have to go through the struglles you experinced in the game in real life.'
                             'Please help them by donating to National Alliance to End Homelessness.', )

        text = Label(self, width=50, text=text)
        text.configure(font=font)
        text.place(relx=0.5, rely=0.3, anchor=CENTER)

        btn_about = Button(self, text="Go Back", bg='black', fg='white',
                           command=lambda: self.controller.show_frame('Home'))
        btn_about.place(relx=0.5, rely=0.5, width=150, height=50, anchor=CENTER)
