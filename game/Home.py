from tkinter import *
from PIL import ImageTk, Image
import os


class Home(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent

        path = "../Assets/purplelight.jpeg"
        self.img = ImageTk.PhotoImage(Image.open(os.path.join(self.controller.dirname, path)))

        background_label = Label(self, image=self.img)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        btn_start = Button(self, text="Start", bg='black', fg='white', font=self.controller.font,
                           command=lambda: self.controller.show_frame('Start'))
        btn_start.place(relx=0.5, rely=0.3, width=150, height=50, anchor=CENTER)

        btn_about = Button(self, text="About Game", bg='black', fg='white', font=self.controller.font,
                           command=lambda: self.controller.show_frame('About'))
        btn_about.place(relx=0.5, rely=0.45, width=150, height=50, anchor=CENTER)

        # btn_donate = Button(self, text="Donate", bg='black', fg='white', font=self.controller.font,
                            # command=lambda: self.controller.show_frame('Donate'))
        # btn_donate.place(relx=0.5, rely=0.6, width=150, height=50, anchor=CENTER)
