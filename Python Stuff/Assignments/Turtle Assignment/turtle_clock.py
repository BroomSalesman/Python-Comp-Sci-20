# Lengths of clock hands:
# second hand will be red
# minute and hour hand will be same colors (any dark color)

import turtle
import keyboard
import datetime
import time

def turtle_clock(the_turtle, the_window, input_method):
    background_color = "grey40"
    the_window.bgcolor(background_color)
    the_window.setup(1000, 1000)

    def draw_clock(any_turtle, any_window):
        any_turtle.penup()
        any_turtle.goto(0, 250)
        #any_turtle.setheading()

        any_turtle.pensize(20)
        any_turtle.pencolor("gold")

        any_turtle.pendown()
        any_turtle.fillcolor("grey80")
        any_turtle.begin_fill()
        any_turtle.circle(radius = 250)
        any_turtle.end_fill()


    draw_clock(the_turtle, the_window)





canvas = turtle.Screen()
canvas.register_shape("Schellenturtle.gif")

bob = turtle.Turtle()
bob.shape("Schellenturtle.gif")

turtle_clock(bob, canvas, "pass")
