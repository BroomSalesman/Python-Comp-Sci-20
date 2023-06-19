# pylint: disable= line-too-long, missing-module-docstring, invalid-name,

# sourcery skip: assign-if-exp
import turtle
import time
import os
import easygui
from turtle_thermometer import *


# current_directory = os.path.dirname(__file__)          # see comments below (lines 17 to 2)

cool_emoji_img_path = os.path.join(os.path.dirname(__file__), "smiley-sunglasses-emoji.png") # This stuff was a wild adventure to get the image to work. Turns out it wasn't file path problems
microbit_pic_img_path = os.path.join(os.path.dirname(__file__), "microbit-pic.png")                 # Turtle canvas would pop up if I set up turtle before using images in message boxes, which would return an error
oops_pic_img_path = os.path.join(os.path.dirname(__file__), "oops.jpg")                                                                                # I commented a bunch about it too, which was commenting about my progress on making it work.


easygui.msgbox(
            msg =  "Welcome to my Python Turtle module program",
            title = "Welcome",
            image = cool_emoji_img_path,
            ok_button = "Click on me or my friend above",
            )

skip_start = easygui.buttonbox(msg = "If you want to skip the introduction and how-to's of this program, press skip.\n"
                               "It is advised you don't skip if this is your first time using this program.",
                               title = "Choose Wisely", choices = ("Continue", "Skip"))



################# Explanation/description of program. Runs only if user chooses 'Continue' (see above)  #############################

# If user chose to continue, then all the following will run.
if skip_start == "Continue":

    # Easygui message box informing users to get their microbit if they one.
    easygui.msgbox(msg = "If you have a microbit laying around, you may want to use it for this program. It's fine if you don't have one too."
                          "\nIf you do have a microbit, plug it in and make sure its connected properly",
                          title = "Heads Up", image = microbit_pic_img_path, ok_button = "Click on me or ^^^^^")


    # Easygui message box
    easygui.msgbox(msg = "In this program, you will have two options to choose from, a clock and a thermometer", title = "What To Expect", ok_button = "I see")


    # Easygui message box explaining the thermometer program
    easygui.buttonbox(msg = "If you choose to try the thermometer, you can use your microbit can detect the temperature.\n"
                   "Then the temperature will be drawn out as a mercury thermometer (the glass ones with the red liquid inside).\n"
                   "If you do not have a microbit,  you can simply choose the temperature.\n"
                   "The thermometer range will be from 5 to 35 degrees celsius (and no, there won't be fahrenheit. Stupid America...)\n"
                   "There is a range so users dont think of trying to reach -40 by pouring liquid nitrogen over their microbits or trying to microwave it.",
                   title = "Thermometer Explanation", choices = ("Sounds good", "Who you calling stupid!"))


    # Easygui message box explaining the clock program
    easygui.msgbox(msg = "The clock will not depend on the microbit, but you can use the button on your microbit and it will take your local time and then display it on a clock.\n"
                   "The clock will not change automatically as the time changes, but it will update if you press R on your keyboard, or a button on your microbit\n"
                   "You can also manually input the time you want You can still press R or a button to reload the time if you set a fake time",
                   title = "Clock Explanation", ok_button =  "JUST GET TO IT!!!")





################ End of start-up information, if users decided to skip, code starts from here #################

# Asks user if they want to use microbit.
choose_microbit = easygui.buttonbox(msg="Do you have a microbit that you want to use?", title="Microbit?", choices=("Yessirree Bob", "Nah"))

if choose_microbit == "Nah":
    input_method = "keyboard"
else:
    input_method = "microbit"

# If user chooses to use microbit, they go through the steps to connect it and confirm connection
if input_method == "microbit":
    easygui.msgbox(msg = "If you already have your microbit connected, ignore the what's below.\n"
                   "Now you will be given instructions to connect your microbit in the terminal.\n"
                   "Follow the instructions in the terminal to successfully connect your microbit.\n"
                   "After you connect, and you see TESTING scroll on your microbit, then press 'connected' on the pop up box.",
                   title = "Connect Microbit", ok_button = "Wait no not the terminal nooooooooo!!!!")

    # Imports microbit and instructions in terminal are shown to connect microbit to machine
    import microbit


    # If connection successful, and microbit functional, it displays TESTING on the LED matrix, changing letter each 200 miliseconds.
    easygui.msgbox(msg= " Look down on your microbit. It should display letters that spell out 'TESTING')", title = "Check For Connection", ok_button = "uh okay")
    for char in "TESTING" * 3:
            microbit.display.show(char)
            time.sleep(0.2)


    # Asks user to confirm if the test worked or not
    test_confirmation = easygui.buttonbox(msg = "Did you see TESTING on your microbit?", title = "Test Confirmation", choices = ("Yes", "No"))

    # Changes input method for the turtle program to keyboard since user's microbit didn't display 'TESTING'
    if test_confirmation == "No":
        input_method = "keyboard"
        easygui.msgbox(msg = "In that case, you will have to use your keyboard for this program,\n or you can exit the program and try again.",
                       title = "Microbit Problems", image = oops_pic_img_path, ok_button = "Awww...")







######################### User Turtle Drawing Selection #################################
user_selection = easygui.buttonbox(msg = "Choose the turtle drawing you want to try:", title = "Selection", choices = ("Thermometer", "Clock"))



# Calls the function from the turtle_thermometer.py file
if user_selection == "Thermometer":
    easygui.msgbox(msg = "Press E twice while in the turtle program to manually enter a temperature.\n"
                   "Press any microbit button to refresh the turtle drawing to match temperature reading on your microbit (if you are using one)\n"
                   "Press Q twice to exit the program. Keep in mind you will have to run the python file again after you exit the program.",
                   title = "Controls", ok_button = "Got it")

    #canvas = turtle.Screen()
    #canvas.bgcolor("gray40")
    #canvas.register_shape("Schellenturtle.gif")

    #bob = turtle.Turtle()
    #bob.color("black")
    #bob.pensize(7)
    #bob.shape("Schellenturtle.gif")

    #turtle_thermometer(bob, canvas)





print("\n\n\n\n\n\n\n\n")








