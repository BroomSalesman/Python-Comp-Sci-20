import turtle
import microbit as mcb

window = turtle.Screen()
monkey = turtle.Turtle()
monkey.color("Yellow")
monkey.shape("turtle")

# Time in milliseconds between button presses
DOUBLE_PRESS_TIME = 500

last_pressed_time = 0
double_pressed = False
pen_down = True

while True:

    x = mcb.accelerometer.get_x()
    print(x)

    if x < -400:
        monkey.left(5)

    elif x > 400:
        monkey.right(5)

    # Check if button A is pressed
    if mcb.button_a.is_pressed():
        # Calculate time since last button press
        current_time = mcb.running_time()
        time_since_last_press = current_time - last_pressed_time

        if time_since_last_press < DOUBLE_PRESS_TIME:
            # Double press detected

            # Detects whether to put pen down or up
            if pen_down == True:
                monkey.penup()
                # add microbit display code later
                last_pressed_time = current_time

            elif pen_down == False:
                monkey.pendown()
                last_pressed_time = current_time

        # If double press not detected, turtle moves
        elif time_since_last_press > DOUBLE_PRESS_TIME:
            if mcb.button_a.is_pressed():
                while mcb.button_a.is_pressed():
                    monkey.forward(5)

            if mcb.button_b.is_pressed():
                while mcb.button_b.is_pressed():
                    monkey.backward(5)
