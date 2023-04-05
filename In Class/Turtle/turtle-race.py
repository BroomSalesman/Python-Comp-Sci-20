import turtle
import random


STARTING_LINE = -300
FINISH_LINE = 250

#setup window and turtles

window = turtle.Screen()
window.bgcolor("DarkGreen")

bob = turtle.Turtle()
bob.shape("turtle")
bob.color("yellow")
bob.penup()

stuart = turtle.Turtle()
stuart.shape("turtle")
stuart.color("LightGoldenrod2")
bob.penup()

#draw the finish line
ref = turtle.Turtle()
ref.pensize(3)
ref.penup()
ref.goto(FINISH_LINE, 175)
ref.pendown()
ref.goto(FINISH_LINE, -175)
ref.hideturtle()

#send to start line
bob.goto(STARTING_LINE, 100)
stuart.goto(STARTING_LINE, -100)

#do the race!
while bob.xcor() < FINISH_LINE and stuart.xcor() < FINISH_LINE:
    bob_step = random.randrange(1, 10)
    stuart_step = random.randrange(1, 10)
    
    bob.forward(bob_step)
    stuart.forward(stuart_step)
    
#victory message
if bob.xcor() > stuart.xcor():
    