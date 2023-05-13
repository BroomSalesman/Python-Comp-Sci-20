import turtle
import microbit as mcb
import time

window = turtle.Screen()
window.bgcolor("Gray")
monkey = turtle.Turtle()
monkey.color("Yellow")
monkey.shape("turtle")
pen_down = True

#Makes a list of letters for microbit display to show
pen_down_words = list("PenDown")
pen_up_words = list("PenUp")


DOUBLE_PRESS_TIME = 500

while True:
    x = mcb.accelerometer.get_x()
    # Turtle turns left when microbit is tilted enough to the left
    if x < -300:
        monkey.left(10)

    # Turtle turns right
    elif x > 300:
        monkey.right(10)

    if mcb.button_b.is_pressed():
        while mcb.button_b.is_pressed():
            monkey.forward(5)

    if mcb.button_a.was_pressed():
        if pen_down == True:
            monkey.penup()
            pen_down = False
            for letter in pen_up_words:
                mcb.display.show(letter)
                mcb.sleep(450)

        elif pen_down == False:
            monkey.pendown()
            pen_down = True
            for letter in pen_down_words:
                mcb.display.show(letter)
                mcb.sleep(450)
