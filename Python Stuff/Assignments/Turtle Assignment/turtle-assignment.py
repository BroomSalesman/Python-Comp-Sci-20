import turtle
import datetime
import easygui
import os


# current_directory = os.path.dirname(__file__)          # see comments below (lines 16 to 2)

image_path = os.path.join(os.path.dirname(__file__), "smiley-sunglasses-emoji.png") # the final solution that worked (relating to comments below. See above as well.)

easygui.msgbox(
            msg =  "Welcome to my Python Turtle module program",
            title = "Welcome",
            image = image_path
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
                                                                                                               # Whew! that was a lot of commenting. I do have a feel for documenting for my final project now, I guess.
                                                                                                               #And it turns out I didn't even need the  os  module, moving the turtle lines made the image work without file path.



canvas = turtle.Screen()
canvas.bgcolor("dark grey") #change this later

bob = turtle.Turtle()
bob.shape("turtle")
bob.color("yellow")
bob.pensize(5)






























