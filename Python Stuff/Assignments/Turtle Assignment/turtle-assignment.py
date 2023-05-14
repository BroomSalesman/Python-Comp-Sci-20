# pylint: disable= line-too-long, missing-module-docstring, invalid-name,

# sourcery skip: assign-if-exp
import turtle
import time
import os
import easygui

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
                               title = "Choose Wisely", choices = ("Skip", "Continue"))



################# Explanation/description of program. Runs only if user chooses 'Continue' (see above)  #############################

# If user chose to continue, then all the following will run.
if skip_start == "Continue":

    # Easygui message box informing users to get their microbit if they one.
    easygui.msgbox(msg = "If you have a microbit laying around, you may want to use it for this program. It's fine if you don't have one too."
                          "\nIf you do have a microbit, plug it in and make sure its connected properly",
                          title = "Heads Up", image = microbit_pic_img_path, ok_button = "Click on me or ^^^^^")


    # easygui message box
    easygui.msgbox(msg = "In this program, you will have two options to choose from, a clock and a thermometer", title = "What To Expect", ok_button = "I see")

    # easygui message box explaining the thermometer
    easygui.msgbox(msg = "If you choose thermometer, and have a microbit, your microbit can detect the temperature.\n"
                   "Then, it will draw out a thermometer with the temperature.\n"
                   "If you do not have a microbit, just select 'No Microbit'. This way, you can just enter the temperature.\n"
                   "The thermometer range will be from -5 to 30 degrees celsius (because this is Canada, eh).\n"
                   "There is a range so users dont think of trying to reach -40 with their microbits.",
                   title = "Thermometer Explanation", ok_button = "Sounds good")

    # easygui message box explaining the clock
    easygui.msgbox(msg = "The clock will not depend on the microbit except for using a button, and it will take your local time and then display it on a clock.\n"
                   "It will not change automatically as the time changes, but it will update if you press R on your keyboard, or a button on your microbit\n"
                   "You can also input the time you want, but you can only input it once, otherwise you'll have to re-run the program.\n"
                   "You can still press R or a button to reload the time if you set a fake time",
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
    easygui.msgbox(msg = "Now you will be given instructions in the terminal.\n"
                   "Follow the instructions in the terminal to successfully connect your microbit.\n"
                   "After you connect, and you see TESTING scroll on your microbit, then press 'connected' on the pop up box.",
                   title = "Connect Microbit", ok_button = "Wait no not the terminal nooooooooo!!!!")

    # Imports microbit and instructions in terminal are shown to connect microbit
    import microbit


    # If connection successful, and microbit functional, it displays TESTING on the LED matrix, changing letter each 200 miliseconds.
    for i in "TESTING" * 3:
            microbit.display.show(i)
            time.sleep(0.2)


    # Asks user to confirm if the test worked or not
    test_confirmation = easygui.choicebox(msg = "Did you see TESTING on your microbit?", title = "Test Confirmation", choices = ("Yes", "No"))

    # Changes input method for the turtle program to keyboard since user's microbit didn't display 'TESTING'
    if test_confirmation == "No":
        input_method = "keyboard"
        easygui.msgbox(msg = "In that case, you will have to use your keyboard for this program,\n or you can exit the program and try again.",
                       title = "Microbit Problems", image = oops_pic_img_path, ok_button = "Awww...")










######################### User Turtle Drawing Selection #################################
easygui.buttonbox(msg = "Choose the turtle drawing you want to see:", title = "Selection", choices = ("Thermometer", "Clock"))





canvas = turtle.Screen()
canvas.bgcolor("dark grey") #change this later

bob = turtle.Turtle()
bob.shape("turtle")
bob.color("yellow")
bob.pensize(5)





print("\n\n\n\n\n\n\n\n")



















