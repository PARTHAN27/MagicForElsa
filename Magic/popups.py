import time
from tkinter import Tk, Label

from task1.task import web

from Magic import tkinterlib, theme, chat_client
from Magic.tkinterlib import TButton


def popups(srch: str):
    """A yes or no gui box to know if the user needs to search things in the internet"""
    popupWindow = Tk()

    screen_height = popupWindow.winfo_screenheight()
    screen_width = popupWindow.winfo_screenwidth()
    tkinterlib.tkinter_initialise(popupWindow, x=screen_width - 130, y=screen_height - 130)

    def srchYes(event=""):
        popupWindow.destroy()
        web(srch)

    Yes = TButton(popupWindow, text="Yes", command=srchYes)
    No = TButton(popupWindow, text="No", command=popupWindow.destroy)
    Yes.grid(row=1, column=0)
    No.grid(row=1, column=1)
    popupWindow.mainloop()


def resetelsapopup():
    """Gui and backend for resetting Elsa"""
    import os
    import shutil
    from talk1.talk1 import talk
    from pathlib import Path

    popupWindow = Tk()
    bg_colour, text_color, button_colour = theme.read_theme()
    screen_height, screen_width = popupWindow.winfo_screenheight(), popupWindow.winfo_screenwidth()
    tkinterlib.tkinter_initialise(popupWindow, x=int(screen_width / 2), y=int(screen_height / 2))
    popupWindow.geometry(f"193x50+{int(screen_width / 2)}+{int(screen_height / 2)}")
    talk("Are you sure that you want to reset Elsa")
    Label(popupWindow, text="Are you sure you want to reset Elsa?", fg=text_color, bg=bg_colour).place(x=0, y=0)

    def Yes(event=""):
        talk("Please wait for a moment. Elsa is being reset")
        talk("Just run elsa after it shutdowns")
        print("Resetting Elsa")
        time.sleep(1)
        shutil.rmtree(Path(os.getcwd() + "\\resources"))
        try:
            chat_client.closeClient()
        except:
            pass
        exit()

    Yes = TButton(popupWindow, text="Yes", command=Yes)

    No = TButton(popupWindow, text="No", command=popupWindow.destroy)
    Yes.place(x=60, y=20)
    No.place(x=100, y=20)
    popupWindow.mainloop()
