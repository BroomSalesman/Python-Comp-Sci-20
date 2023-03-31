import turtle
import microbit as mcb

window = turtle.Screen()
monkey = turtle.Turtle()
monkey.color("Yellow")
monkey.shape("turtle")

while True:
    x = mcb.accelerometer.get_x()
    print(x)

    if mcb.button_a.was_pressed():
        print("Right!")
        monkey.forward(5)
    
    if mcb.button_b.was_pressed():
        print("LEFT!")
        monkey.backward(5)


