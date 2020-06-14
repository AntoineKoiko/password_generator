#!/bin/env python3
from tkinter import *
import string
from random import choice

#constante var
BG_COLOR = "#5c3314"
SAVE_PATH = "password.txt"
SECRET_KEY = 12

#encode / decode msg (for password)
def my_encode(msg):
    encoded = ""

    for let in msg:
        encoded += chr(ord(let) + SECRET_KEY)
    return encoded

def my_decode(msg):
    decoded = ""

    for let in msg:
        decoded += chr(ord(let) - SECRET_KEY)
    return decoded

#class with button commands
class Button_cmd():

    def __init__(self):
        pass

    def generate_password(self):
        length = 12
        possible_chars = string.ascii_letters + string.punctuation + string.digits
        password = "".join(choice(possible_chars) for let in range(length))
        app.paswd_entry.delete(0, END)
        app.paswd_entry.insert(0, password)
        app.cur_pass = password

    def save_password(self):
        with open(SAVE_PATH, "a+") as file:
            file.write(my_encode(app.cur_pass) + "\n")

#create main window
class Window():

    def __init__(self):
        self.wind = Tk()
        self.config_window()
        self.command = Button_cmd()
        self.cur_pass = ""

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
        self.set_save_button()
        self.set_menu_bar()
    
    def set_title(self):
        lb_title = Label(self.wind, text='Password Generator', bg=BG_COLOR, fg="white", font=("arial", 40))
        lb_title.pack(expand=YES, side=TOP)

    def set_paswd_lb(self):
        lb_paswd = Label(self.central_fram, text = 'Password', bg=BG_COLOR, fg="white", font=("arial", 32))
        lb_paswd.grid(row = 0, column = 0)
    
    def set_paswd_entry(self):
        self.paswd_entry.grid(row = 1, column = 0)
    
    def set_generate_button(self):
        generate_button = Button(self.central_fram, text = 'Generate', font=("arial", 24), bg=BG_COLOR,
            command=self.command.generate_password)
        generate_button.grid(row = 2, column = 0)

    def set_save_button(self):
        save_button = Button(self.central_fram, text = 'Save password', font=("arial", 24), bg=BG_COLOR,
            command=self.command.save_password)
        save_button.grid(row = 4, column = 0)

    def set_menu_bar(self):
        menu_bar = Menu(self.wind)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Generate", command=self.command.generate_password)
        file_menu.add_command(label="My password", command=open_password_list)
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=self.wind.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        self.wind.config(menu=menu_bar)


"""
Window tho see our password
"""

def display_password(top):
    lines = []

    with open(SAVE_PATH, "r") as file:
        lines = file.readlines()
    for idx, line in enumerate(lines):
        paswd = my_decode(line[:-1])
        list_passwd_lb = Label(top, text = f'Password : {paswd}', bg="blue", font=("arial", 12))
        list_passwd_lb.grid(row = idx, column = 0)
    

def open_password_list():
    top = Toplevel(app.wind)
    top.title("My password")
    top.geometry("480x300")
    top.config(background="blue")

    display_password(top)
    top.mainloop()

app = Window()
pass_list = []

#mainloop
app.wind.mainloop()