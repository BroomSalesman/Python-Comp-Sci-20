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


start_up_info = easygui.buttonbox(
    msg = ("If you want to skip the introduction and how-to's of this program, press skip."
           "\nIt is advised you don't skip if this is your first time using this program."),
    title = "Choose Wisely",
    choices = ("Skip", "Continue")
)

if start_up_info == "Continue":
    easygui.msgbox(
        msg = ("If you have a microbit laying around, you may want to use it for this program. It's fine if you don't have one too."
               "\nIf you do have a microbit, plug it in and make sure its connected properly"),
        title = "Heads Up",
        image = microbit_pic_img_path,
        ok_button = "Click on me or ^^^^^",
    ) # type: ignore

    easygui.msgbox(
        msg = "In this program, you will have two options to choose from, a clock or a thermometer.",
        title = "What To Expect",
        ok_button = "I see"
        )

    easygui.msgbox(
        msg = ("If you choose thermometer, and have a microbit, your microbit can detect the temperature."
               "\nThen, it will draw out a thermometer with the temperature."
               "\nIf you do not have a microbit, just select 'No Microbit'. This way, you can just enter the temperature."
               "\nThe thermometer range will be from -5 to 30 degrees celsius (because this is Canada, eh)."
               "\nThere is a range so users dont think of trying to reach -40 with their microbits."),
        title = "Thermometer Explanation",
        ok_button = "Sounds good."
        )

    easygui.msgbox(
        msg = ("The clock will not use a microbit at all, and it will take your local time and then display it on a clock."
               "\nIt will not change automatically as the time changes, but it will update if you press R"
               "\nYou can also input the time you want, but you can only input it once, otherwise you'll have to re-run the program."
               "\nYou can still press R to reload the time if you set a fake time"),
        title = "Clock Explanation",
        ok_button =  "JUST GET TO IT!!!"
    )

choose_microbit = easygui.buttonbox(msg = "Do you have a microbit that you want to use?", title = "Microbit?", choices = ("Yessirree bob", "Nah")

if choose_microbit == "Yessirree bob":

    easygui.msgbox(
        msg =("Now you will be given instructions in the terminal."
              "\nFollow the instructions to successfully connect your microbit."),
        title = "Connect Microbit"
        ok_button = "Wait the terminal nooooooooo!!!!"


canvas = turtle.Screen()
canvas.bgcolor("dark grey") #change this later

bob = turtle.Turtle()
bob.shape("turtle")
bob.color("yellow")
bob.pensize(5)





print("\n\n\n\n\n\n\n\n")




















