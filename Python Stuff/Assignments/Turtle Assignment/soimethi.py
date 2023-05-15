
import time
import turtle
import easygui



temperature = easygui.choicebox(msg="Enter a temperature", title="Thermometer Temperature", choices=iter(range(-5, 36)))



canvas = turtle.Screen()
canvas.bgcolor("black")

bob = turtle.Turtle()
bob.shape("turtle")
bob.color("yellow")
bob.pensize(5)


bob.goto(0, -300)
bob.left(90)
turtle.trace(G0)
for i in range(360):
    bob.forward

bob.forward(10)
bob.penup()
bob.forward()


