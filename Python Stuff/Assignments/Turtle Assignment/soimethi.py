import microbit
import time
import turtle
import easygui



temperature = easygui.choicebox(
    msg="Enter a temperature",
    title="Thermometer Temperature",
    choices=iter(range(-5, 36)),
)

canvas = turtle.Screen()
canvas.bgcolor("dark grey")

bob = turtle.Turtle()
bob.shape("turtle")
bob.color("yellow")
bob.pensize(5)


