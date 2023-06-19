import turtle
import time
import microbit
# maybe add auto screen res canvas setup later
# also add a little turtle that loop writing (press q to exit the program)
# and above that "press R to refresh"
# and "press e to manually choose a temperature"

def turtle_thermometer(the_turtle, the_window):
    the_turtle.penup()

    the_turtle.right(90)
    the_turtle.forward(280) # Current location 0, -280
    the_turtle.right(90)

    print(f"{the_turtle.pos()}")
    the_turtle.pendown()

    # The turtle keeps its color, but fills anything inside the outline red. So the outline is black, fill is red.
    the_turtle.fillcolor("red")
    the_turtle.begin_fill()
    the_turtle.circle(radius = 40)
    the_turtle.end_fill()


    print(f"{the_turtle.pos()}")

    the_turtle.color("red")
    the_turtle.pensize(7)
    the_turtle.penup()

    the_turtle.goto(-26, -290)


    #Drawing and filling in bottom part of thermometer, above the round part of it.
    the_window.tracer(5)
    the_turtle.pendown()
    the_turtle.right(90)

    the_turtle.fillcolor("red")
    the_turtle.begin_fill()

    for half in range(2):
        the_turtle.forward(20)
        the_turtle.right(90)
        print(f"{the_turtle.pos()} here")
        the_turtle.forward(50) # distance from -26 to 26 (on x-axis) because 52 made sides noticeably
        the_turtle.right(90)

    the_turtle.end_fill()


    # Creates left side of thermometer
    the_turtle.color("black")
    the_turtle.goto(-26, 330)
    print()

    # Draws a semicircle to create the top of thermometer.
    the_turtle.circle(radius = -26, extent = 180)  # post-execution position: 26, 270
    print(f"{the_turtle.pos()}")


    # Creates right side of thermometer
    the_window.tracer(1)
    the_turtle.goto(26, -290)
    print(f"{the_turtle.pos()}")

    # Draws every sub-division tick and division tick in thermometer
    # Every sub-division tick is 20 pixels apart from each other
    # Every major division tick is 100 pixels away.
    the_turtle.penup()
    the_turtle.goto(-26, -290)
    the_turtle.left(180)

    the_turtle.begin_poly()

    for big_tick in range(6):
        the_turtle.pensize(6)
        the_turtle.forward(20)
        the_turtle.right(90)
        the_turtle.forward(13)
        the_turtle.pendown()
        the_turtle.forward(26)
        the_turtle.penup()
        the_turtle.backward(39)
        the_turtle.left(90)
        the_turtle.pensize(4)

        for sub_tick in range(4):
            the_turtle.forward(20)
            the_turtle.right(90)
            the_turtle.pendown()
            the_turtle.forward(13)
            the_turtle.penup()
            the_turtle.backward(13)
            the_turtle.left(90)

    the_turtle.forward(20)
    the_turtle.right(90)
    the_turtle.forward(13)
    the_turtle.pendown()
    the_turtle.forward(26)
    the_turtle.penup()

    the_turtle.end_poly()

    the_turtle.goto(100, 290)
    the_turtle.write("Press E to enter a value for the thermometer.")
    the_turtle.goto(100, 280)
    the_turtle.write("FOR MICROBIT USERS: Press any button on your microbit to detect temperature and refresh readings.")
    the_turtle.goto(100, 270)
    the_turtle.write("Press Q to exit the program.")

    # Thermometer drawn now.

def thermometer_update(input_method):
    while True:
        if microbit.button_a.was_pressed() or microbit.button_b.was_pressed():
            bob.



canvas = turtle.Screen()
canvas.bgcolor("grey40")

bob = turtle.Turtle()
bob.color("black")
bob.pensize(7)
#bob.shape("Schellenturtle.gif")

turtle_thermometer(bob, canvas)

turtle.done()
