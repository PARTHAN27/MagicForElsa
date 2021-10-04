import os
from tkinter.colorchooser import askcolor


def read_theme():
    """[Reads the theme from the initial.elsa file]

    Returns:
        [bg_colour,text_colour,button_colour]: [The background,text/font and the button colour found]
    """
    try:
        initpth = os.getcwd() + "\\resources\\ initial.elsa"
        with open(initpth) as f:
            datas = f.read()
        colours = datas.split(";")
        bg_colour = colours[0].rstrip().lstrip()
        text_color = colours[1].rstrip().lstrip()
        colours = colours[2].split("\n")

        button_colour = colours[0].rstrip().lstrip()

        return bg_colour, text_color, button_colour
    except Exception as e:
        print("initial.elsa is corrupted")
        print(e)


def theme_writer(bg_colour, font_colour, button_colour):
    initpth = os.getcwd() + "\\resources\\ initial.elsa"
    with open(initpth, "w") as f:
        f.write(
            f"{bg_colour};{font_colour};{button_colour}\n #The order is bg,font color,button colour \n#Please remember to use ';' to separate colours :D"
        )

    del bg_colour, font_colour, button_colour


def new_background_colour(event=""):
    color = askcolor()
    bg_colour, text_color, button_colour = read_theme()
    if color[1] != None:
        theme_writer(color[1], text_color, button_colour)


def new_font_colour(event=""):
    color = askcolor()
    bg_colour, text_color, button_colour = read_theme()
    if color[1] != None:
        theme_writer(bg_colour, color[1], button_colour)


def new_button_colour(event=""):
    color = askcolor()
    bg_colour, text_color, button_colour = read_theme()
    if color[1] != None:
        theme_writer(bg_colour, text_color, color[1])
