#!/bin/env python3
from tkinter import *

#constante var
BG_COLOR = "#5c3314"

#create main window
class Window():

    def __init__(self):
        self.wind = Tk()
        self.config_window()

        #center with text entry and button
        self.central_fram = Frame(bg=BG_COLOR)

        #text input for password
        self.paswd_entry = Entry(self.central_fram, font=("arial", 20))

        #initialize permanent widgets
        self.set_wiidgets()
        self.central_fram.pack(expand=YES)
       
    def config_window(self):
        self.wind.geometry("1280x720")
        self.wind.minsize(720, 480)
        self.wind.maxsize(1280, 720)
        self.wind.title("My Password Generator")
        self.wind.config(background=BG_COLOR)

    def set_wiidgets(self):
        self.set_title()
        self.set_paswd_lb()
        self.set_paswd_entry()
        self.set_generate_button()
    
    def set_title(self):
        lb_title = Label(self.wind, text='Password Generator', bg=BG_COLOR, fg="white", font=("arial", 40))
        lb_title.pack(expand=YES, side=TOP)

    def set_paswd_lb(self):
        lb_paswd = Label(self.central_fram, text = 'Password', bg=BG_COLOR, fg="white", font=("arial", 32))
        lb_paswd.grid(row = 0, column = 0)
    
    def set_paswd_entry(self):
        self.paswd_entry.grid(row = 1, column = 0)
    
    def set_generate_button(self):
        generate_button = Button(self.central_fram, text = 'Generate', font=("arial", 24), bg=BG_COLOR)
        generate_button.grid(row = 2, column = 0)


#mainloop
app = Window()
app.wind.mainloop()