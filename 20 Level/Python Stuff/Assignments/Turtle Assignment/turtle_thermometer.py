import turtle
import keyboard
import easygui
import sys
import time
# maybe add auto screen res canvas setup later
# also add a little turtle that loop writing (press q to exit the program)
# and above that "press R to refresh"
# and "press e to manually choose a temperature"

def turtle_thermometer(the_turtle, the_window, input_method):
    #Over riding turtle settings if Turtle object properties defined outside of function (that sounded fancy)
    background_color = "grey40"
    the_window.setup(1000, 750)
    the_window.bgcolor(background_color)

    the_turtle.color("black")
    the_turtle.pensize(7)
    the_turtle.penup()


    # Moves downward to draw rounded bottom part of thermometer
    the_turtle.right(90)
    the_turtle.forward(280) # Current location 0, -280
    the_turtle.right(90)


    # The turtle keeps its color, but fills anything inside the outline red. In this case, the outline is black and fill is red.
    the_turtle.pendown()
    the_turtle.fillcolor("red")
    the_turtle.begin_fill()
    the_turtle.circle(radius = 40)
    the_turtle.end_fill()

    the_turtle.color("red")
    the_turtle.pensize(7)
    the_turtle.penup()

    the_turtle.goto(-26, -290)


    #Drawing and filling in bottom part of thermometer, above the round part of it.
    the_turtle.pendown()
    the_turtle.right(90)

    the_turtle.fillcolor("red")
    the_turtle.begin_fill()

    for half in range(2):
        the_turtle.forward(20)
        the_turtle.right(90)
        the_turtle.forward(50) # distance from -26 to 26 (on x-axis) because 52 made sides noticeably
        the_turtle.right(90)

    the_turtle.end_fill()


    # Creates left side of thermometer
    the_turtle.color("black")
    the_turtle.goto(-26, 330)

    # Draws a semicircle to create the top of thermometer.
    the_turtle.circle(radius = -26, extent = 180)  # post-execution position: 26, 270


    # Creates right side of thermometer
    the_turtle.goto(26, -290)

    # Draws every sub-division tick and division tick in thermometer
    # Every sub-division tick is 20 pixels apart from each other
    # Every major division tick is 100 pixels away.

    def thermometer_ticks(any_turtle):
        any_turtle.penup()
        any_turtle.color("black")
        any_turtle.goto(-26, -290)
        any_turtle.setheading(90)

        for big_tick in range(6):
            any_turtle.pensize(6)
            any_turtle.forward(20)
            any_turtle.right(90)
            any_turtle.forward(13)
            any_turtle.pendown()
            any_turtle.forward(26)
            any_turtle.penup()
            any_turtle.backward(39)
            any_turtle.left(90)
            any_turtle.pensize(4)

            for sub_tick in range(4):
                any_turtle.forward(20)
                any_turtle.right(90)
                any_turtle.pendown()
                any_turtle.forward(13)
                any_turtle.penup()
                any_turtle.backward(13)
                any_turtle.left(90)

        any_turtle.pensize(6)
        any_turtle.forward(20)
        any_turtle.right(90)
        any_turtle.forward(13)
        any_turtle.pendown()
        any_turtle.forward(26)
        any_turtle.penup()

    the_turtle.speed(10)
    thermometer_ticks(the_turtle)

    # Writes controls
    the_turtle.goto(85, 295)
    the_turtle.write("Press E twice to enter a value for the thermometer")
    the_turtle.goto(85, 280)
    the_turtle.write("MICROBIT: Press any button on your microbit to detect temperature and")
    the_turtle.goto(85, 267)
    the_turtle.write("          refresh thermometer reading.")
    the_turtle.goto(85, 255)
    the_turtle.write("Press Q to exit the program. Press out of window then press Q if it isn't responding.")



    def draw_temperature(any_turtle, any_window, mercury_level):
        any_window.tracer(10)
        any_turtle.goto(-22, -270)
        any_turtle.pensize(1)
        any_turtle.pendown()
        any_turtle.color("red")
        any_turtle.fillcolor("red")

        any_turtle.setheading(90)

        any_turtle.begin_fill()
        for half in range(2):
            any_turtle.forward(mercury_level * 20)
            any_turtle.right(90)
            any_turtle.forward(44)
            any_turtle.right(90)
        any_turtle.end_fill() # Position: -22, -270

        any_turtle.penup()
        thermometer_ticks(any_turtle)


    def clear_thermometer(any_turtle, any_window, bg_color):
        any_window.tracer(10)
        any_turtle.speed(0)

        any_turtle.pensize(1)
        any_turtle.color(bg_color)
        any_turtle.penup()

        # To clear thermometer using an under-the-rug method (drawing over it)
        any_turtle.goto(-22, -270)
        any_turtle.fillcolor(bg_color)
        any_turtle.setheading(90)
        any_turtle.pendown()

        any_turtle.begin_fill()
        for half in range(2):
            any_turtle.forward(600)
            any_turtle.right(90)
            any_turtle.forward(44)
            any_turtle.right(90)
        any_turtle.end_fill()

        thermometer_ticks(any_turtle)



    while True:
        if keyboard.is_pressed("e"):
            time.sleep(0.66)

            try:
                temperature = int(easygui.choicebox(msg ="Choose a temperature", title = "Temperature", choices = [i + 5 for i in range(30)]))
                mercury_height = temperature - 5

            except Exception:
                temperature = 5
                mercury_height = 15 -5

            clear_thermometer(the_turtle, the_window, background_color)
            draw_temperature(the_turtle, the_window, mercury_height)

        if keyboard.is_pressed("q"):
            sys.exit()

        if input_method == "microbit":
            import microbit

            if microbit.button_a.was_pressed() or microbit.button_b.was_pressed():
                temperature = microbit.temperature()
                clear_thermometer(the_turtle, the_window, background_color)

                if 5 <= temperature < 30:
                    mercury_height = temperature - 5
                    clear_thermometer(the_turtle, the_window, background_color)
                    draw_temperature(the_turtle, the_window, mercury_height)

                elif temperature > 30:
                    clear_thermometer(the_turtle, the_window, background_color)
                    draw_temperature(the_turtle, the_window, 30)
                    easygui.msgbox(msg = f"Temperature too high for thermometer ({temperature} °C).", title = "Temperature Too High", ok_button = "Aw man")


                elif temperature < 5:
                    clear_thermometer(the_turtle, the_window, background_color)
                    easygui.msgbox(msg = f"Temperature too low for thermometer. ({temperature} °C)", title = "Temperature Too Low", ok_button = "brrrrr")


