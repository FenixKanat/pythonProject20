from tkinter import *
from PIL import ImageTk, Image
import os
import textwrap
import tkinter.font as tkfont


class Start(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        path = "../Assets/purplelight.jpeg"
        self.img = ImageTk.PhotoImage(Image.open(os.path.join(self.controller.dirname, path)))

        background_label = Label(self, image=self.img)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        my_font = tkfont.Font(family="Times New Roman", size=16, weight="bold")  # slant="italic"

        font = tkfont.Font(family="Times New Roman", size=10, weight="bold")

        text = Label(self, text='Please choose a character')
        text.configure(font=my_font)
        text.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.btn_woman_bg = ImageTk.PhotoImage(
            Image.open(os.path.join(self.controller.dirname, '../Assets/btn_woman.jpg')))
        img_label = Label(image=self.btn_woman_bg)

        self.btn_man_bg = ImageTk.PhotoImage(
            Image.open(os.path.join(self.controller.dirname, '../Assets/homeless-man.jpg')))
        img_label = Label(image=self.btn_man_bg)

        btn_male = Button(self, image=self.btn_man_bg)
        btn_female = Button(self, image=self.btn_woman_bg)
        btn_back = Button(self, text="Go Back", bg='black', fg='white',
                          command=lambda: self.controller.show_frame('Home'))

        btn_male.place(relx=0.75, rely=0.35, width=256, height=256, anchor=CENTER)
        btn_female.place(relx=0.25, rely=0.35, width=256, height=256, anchor=CENTER)
        btn_back.place(relx=0.5, rely=0.9, width=150, height=50, anchor=CENTER)

        text_female = textwrap.fill(
            'This is Lisa. She used to work as a preschool teacher. '
            'After she lost both of her children, she got depressed and lost everything she had. '
            'Do you want to help Lisa get back on track?',
            width=50)

        text_female = Label(self, width=50, text=text_female)
        text_female.configure(font=font)
        text_female.place(relx=0.25, rely=0.6, anchor=CENTER)

        text_male = textwrap.fill(
            'This is Edward. He fought hard for his country. '
            "But the PTSD after the things he has been through wouldn't leave him alone. "
            'He needs your help to get his house back. Will you help him?',
            width=50)
        text_male = Label(self, width=50, text=text_male)
        text_male.configure(font=font)
        text_male.place(relx=0.75, rely=0.6, anchor=CENTER)

        btn_ph2f1 = Button(self, text="Story", bg='black', fg='white', font=self.controller.font,
                           command=lambda: self.controller.show_frame('Ph1f1'))
        btn_ph2f1.place(relx=0.5, rely=0.6, width=150, height=50, anchor=CENTER)
