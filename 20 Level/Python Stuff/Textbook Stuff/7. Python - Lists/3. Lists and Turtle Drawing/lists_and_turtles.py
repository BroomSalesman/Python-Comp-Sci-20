import turtle
import random

canvas = turtle.Screen()
canvas.bgcolor("Navy")

bob = turtle.Turtle()
bob.shape("turtle")
bob.pensize(4)
bob.color("hot pink")

history = [[0, 0]]
still_moving = True

while still_moving:
    choice = random.randrange(1, 101)

    if choice < 33:
        bob.left(90)

    if choice > 66:
        bob.right(90)

    x = round((bob.xcor()))
    y = round(bob.ycor())
    current_location = [x, y]

    if current_location in history:
        still_moving = False
        print(history)
    else:
        history.append(current_location)


    bob.forward(15)


