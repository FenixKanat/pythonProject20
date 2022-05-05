from tkinter import *
import tkinter.font as tkfont
from PIL import ImageTk, Image
import os


class About(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        path = "../Assets/purplelight.jpeg"
        self.img = ImageTk.PhotoImage(Image.open(os.path.join(self.controller.dirname, path)))

        background_label = Label(self, image=self.img)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        titleAboutGame = Label(self,
                               text="What you need to know the game",
                               bg='black',
                               fg='white')
        titleGameFont = tkfont.Font(family="Comic Sans MS", size=20, weight="bold")  # slant="italic"
        titleAboutGame.configure(font=titleGameFont)
        titleAboutGame.place(relx=0.5, rely=0.1, anchor=CENTER)

        textAboutGame = Label(self,
                              text="This game lets the user to experience some problems the homeless people live with on daily basis.\n\n "
                                   "The user will get TWO choices when the game starts\n "
                                   "you will be able to read the story of the character you would like to help.\n\n "
                                   "The main goal would be to get your character back on track and healthy.\n\n",
                              bg='black',
                              fg='white')
        aboutGameFont = tkfont.Font(family="Helvetica", size=13, weight="bold")  # slant="italic"
        textAboutGame.configure(font=aboutGameFont)
        textAboutGame.place(relx=0.5, rely=0.3, anchor=CENTER)

        textAboutGame2 = Label(self,
                               text="We thank you for playing our game!", bg='black',
                               fg='yellow')
        aboutGameFont2 = tkfont.Font(family="Courier New", size=14, weight="bold")  # slant="italic"
        textAboutGame2.configure(font=aboutGameFont2)
        textAboutGame2.place(relx=0.5, rely=0.383, anchor=CENTER)

        btn_about = Button(self, text="Go Back", bg='black', fg='white',
                           command=lambda: self.controller.show_frame('Home'))
        btn_about.place(relx=0.5, rely=0.6, width=150, height=50, anchor=CENTER)
