import turtle
import datetime
import easygui
import os


# current_directory = os.path.dirname(__file__)          # see comments below (lines 17 to 2)

cool_emoji_img_path = os.path.join(os.path.dirname(__file__), "smiley-sunglasses-emoji.png") # The final solution that worked (relating to comments below. See above as well.) **FILE PATH WAS NOT PROBLEM**
microbit_pic_img_path = os.path.join(os.path.dirname(__file__), "microbit-pic.png")

easygui.msgbox(
            msg =  "Welcome to my Python Turtle module program",
            title = "Welcome",
            image = cool_emoji_img_path,
            ok_button = "Click on me or my friend above",
            )
            #image = current_directory + "\smiley-sunglasses-emoji.png")  # This took some thinking,  research, experimentation, but the learning process was neat. I could feel my brain cells expanding.
                                                                                                               # 5 minutes later: still got the errors , such as:
                                                                                                               # File "C:\Python311\Lib\tkinter\__init__.py", line 1692, in _configure
                                                                                                               # self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
                                                                                                               # _tkinter.TclError: image "pyimage2" doesn't exist"
                                                                                                               #I found  a solution through ChatGPT, going to keep original code here to show you what I was doing.
                                                                                                               # Sad news, it didnt work in this file. Moved turtle code below (setting up turtle and canvas). Going to see if it works.
                                                                                                               # IT WORKED!!!! Turtle would open for a split second, I don't know why, and it would clash with the easygui msgbox,
                                                                                                               # thus resulting in errors taking me all the way to python environment packages
                                                                                                                   # (like, the files of modules in case environment packages is the wrong terms)
                                                                                                               # The error shown in line 18 is what I mean.
                                                                                                               # Whew! that was a lot of commenting. I have a feel for documenting for my final project now, I guess.
                                                                                                               #And it turns out I didn't even need the  os  module, moving the turtle lines made the image work without exact file path.

easygui.msgbox(
    msg = "If you have a microbit laying around, you may want to use it for this program. It's fine if you don't have one too.\n If you do have a microbit, plug it in and make sure its connected properly",
    title = "Heads Up",
    image = microbit_pic_img_path,
    ok_button = "Click on me or ^^^^^"
)

easygui.msgbox(
    msg = (
        "In this program, you will have two options to choose from, a clock or a thermometer.\n"
        "You can choose to use your microbit for the thermometer (which is the coolest part), but if you don't have one, just input a temperature."
        "")
)

canvas = turtle.Screen()
canvas.bgcolor("dark grey") #change this later

bob = turtle.Turtle()
bob.shape("turtle")
bob.color("yellow")
bob.pensize(5)






























