import turtle
import time
import microbit
# maybe add auto screen res canvas setup later
# also add a little turtle that loop writing (press q to exit the program)
# and above that "press R to refresh"
# and "press e to manually choose a temperature"

def turtle_thermometer(input_method):
    canvas = turtle.Screen()
    canvas.bgcolor("gray40")


    bob = turtle.Turtle()
    bob.color("black")
    bob.pensize(7)

    bob.penup()

    bob.right(90)
    bob.forward(280) # Current location 0, -280
    bob.right(90)

    print(f"{bob.pos()}")
    canvas.tracer(3)
    bob.pendown()
    bob.circle(radius = 40)

    bob.pensize(1)
    for i in range(29):
        bob.right
    print(f"{bob.pos()}")

    canvas.tracer(1)

    print(f"{bob.pos()}")

    bob.color("white")
    bob.pensize(3)

    bob.goto(-26, -290)

    canvas.tracer(5)

    for i in range(7): #end of loop position -26, -276
        bob.right(90)
        bob.forward(1)
        bob.right(90)
        bob.forward(52)
        bob.left(90)
        bob.forward(1)
        bob.left(90)
        bob.forward(52)
    print(f"{bob.pos()}")

    canvas.tracer(1)
    bob.goto(-26, -290)
    bob.right(90)
    bob.forward(500)

turtle_thermometer("hello")
time.sleep(3)
