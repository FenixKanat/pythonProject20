from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as tkfont
import textwrap
import os


class Ph2f1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        path = "../Assets/Phase2.jpg"
        self.img = ImageTk.PhotoImage(Image.open(os.path.join(self.controller.dirname, path)))

        background_label = Label(self, image=self.img)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        font = tkfont.Font(family="Times New Roman", size=16, weight="bold")

        text = textwrap.fill("Because of Lisa's mental health kept on getting worse, "
                             "She couldn't stay at someone's else place and had to make a difficult choice",
                             width=50)

        text = Label(self, width=50, text=text)
        text.configure(font=font)
        text.place(relx=0.5, rely=0.3, anchor=CENTER)

        btn_option1 = Button(self, text="1- Seek shelter ", bg='white', fg='black', font=self.controller.font,
                             command=lambda: self.controller.show_frame('Ph2f2'))
        btn_option1.place(relx=0.5, rely=0.5, width=150, height=50, anchor=CENTER)

        btn_option2 = Button(self, text="2- Submit to a mental health hospital", bg='white', fg='black',
                             font=self.controller.font,
                             command=lambda: self.controller.show_frame('Ph2f3'))
        btn_option2.place(relx=0.5, rely=0.6, width=400, height=50, anchor=CENTER)
