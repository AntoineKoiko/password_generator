#!/bin/env python3
from tkinter import *

#create main window
class Window():
    def __init__(self):
        self.wind = Tk()
        self.config_window()

    def config_window(self):
        self.wind.geometry("1280x720")
        self.wind.minsize(720, 480)
        self.wind.maxsize(1280, 720)
        self.wind.title("My Password Generator")
        self.wind.config(background="#5c3314")
    


#mainloop
app = Window()
app.wind.mainloop()