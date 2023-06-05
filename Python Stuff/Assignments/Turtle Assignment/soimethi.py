
import time
import turtle
import easygui


__temperature__ = easygui.choicebox(msg="Enter a temperature", title="Thermometer Temperature", choices=iter(range(-5, 36)))


canvas = turtle.Screen()
canvas.bgcolor("gray")

bob = turtle.Turtle()
bob.color("yellow")
bob.pensize(3)

bob.penup()
bob.goto(0, -300)
bob.left(90)
bob.pendown()

bob.speed(0.9)
bob.circle(radius = 50, steps = 360)


bob.forward(10)
bob.penup()


time.sleep(4)
