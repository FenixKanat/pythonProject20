from tkinter import *
import os
import tkinter.font as font

from Home import Home
from About import About
from Start import Start
from Donate import Donate
from Ph1f1 import Ph1f1
from Ph1f2 import Ph1f2
from Ph1f3 import Ph1f3
from Ph2f1 import Ph2f1
from Ph2f2 import Ph2f2
from Ph2f3 import Ph2f3
from Ph3f1 import Ph3f1
from Ph3f2 import Ph3f2
from Ph3f3 import Ph3f3
from Ph3f4 import Ph3f4
from Ph4 import Ph4


class Main(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.WINDOW_WIDTH = 700
        self.WINDOW_HEIGHT = 700

        self.title('Game - Homeless')
        self.geometry(str(self.WINDOW_WIDTH) + "x" + str(self.WINDOW_HEIGHT))

        self.dirname = os.path.dirname(__file__)
        self.font = font.Font(size=12, weight="bold")

        self.container = Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for frame in (Home, About, Start, Donate,
                      Ph1f1, Ph1f2, Ph1f3,
                      Ph2f1, Ph2f2, Ph2f3,
                      Ph3f1, Ph3f2, Ph3f3, Ph3f4,
                      Ph4):
            f = frame(self.container, self)
            f.grid(row=0, column=0, sticky="nsew")
            self.frames[frame.__name__] = f

        self.show_frame('Home')
        self.mainloop()

    def show_frame(self, frame):
        self.frames[frame].tkraise()


main = Main()
