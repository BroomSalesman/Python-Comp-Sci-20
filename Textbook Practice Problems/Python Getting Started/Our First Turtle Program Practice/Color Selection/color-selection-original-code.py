'''     Modify the program given below so that before it creates the window, it prompts the 
    user to enter the desired background color. It should store the user's response in a variable, 
    and modify the color of the window according to the user's wishes. Do similar changes to allow 
    the user to set the turtle bree's color as well.

    Hint: you can find a list of permitted color names at https://www.w3schools.com/colors/colors_names.asp . 
    It includes some quite unusual ones, like “PeachPuff” and “HotPink”.'''


# Color Selection

import turtle

# create window, and set it's color
canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

# create the turtle, and it's attributes
bree = turtle.Turtle()
bree.color("blue")
bree.pensize(3)

# draw!
bree.forward(100)
bree.right(60)
bree.forward(100)
