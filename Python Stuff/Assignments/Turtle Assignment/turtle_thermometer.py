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
    canvas.register_shape("Schellenturtle.gif")


    bob = turtle.Turtle()
    #bob.shape("Schellenturtle.gif")
    bob.color("black")
    bob.pensize(7)
    bob.penup()

    bob.right(90)
    bob.forward(280) # Current location 0, -280
    bob.right(90)

    print(f"{bob.pos()}")
    canvas.tracer(3)
    bob.pendown()

    # The turtle keeps its color, but fills anything inside the outline red. So the outline is black, fill is red.
    bob.fillcolor("red")
    bob.begin_fill()
    bob.circle(radius = 40)
    bob.end_fill()


    bob.color("black")
    bob.circle(radius = 40)
    print(f"{bob.pos()}")

    canvas.tracer(1)

    print(f"{bob.pos()}")


    bob.color("red")
    bob.pensize(7)
    bob.penup()

    bob.goto(-26, -290)


    #Drawing and filling in bottom part of thermometer, above the round part of it.
    canvas.tracer(5)
    bob.pendown()
    bob.right(90)

    bob.fillcolor("red")
    bob.begin_fill()

    for half in range(2):
        bob.forward(20)
        bob.right(90)
        print(f"{bob.pos()} here")
        bob.forward(50) # distance from -26 to 26 (on x-axis), subtract 2 to make sides even
        bob.right(90)

    bob.end_fill()

   # reference_distance1 = bob.distance()
    #bob.goto()

    # Creates left side of thermometer
    bob.color("black")
    bob.goto(-26, 330)
    print()

    # Draws a semicircle to create the top of thermometer.
    bob.circle(radius = -26, extent = 180)  # post-execution position: 26, 270
    print(f"{bob.pos()}")
    bob.stamp()
    # Creates right side of thermometer
    canvas.tracer(1)
    bob.goto(26, -290)
    print(f"{bob.pos()}")

    # Draws every sub-division tick and division tick in thermometer
    bob.penup()
    bob.goto(-26, -270)
    bob.left(180)

    for i in range(6):
        bob.pensize(6)
        bob.right(90)
        bob.forward(13)
        bob
        bob.backward(13)
       bob.left(90)
       for i in range(5):
           bob.penup()

    #for i in range()


turtle_thermometer("hello")

turtle.done()
