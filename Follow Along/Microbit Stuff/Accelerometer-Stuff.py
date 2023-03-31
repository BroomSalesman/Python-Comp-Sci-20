import turtle
import microbit as mcb

window = turtle.Screen()
monkey = turtle.Turtle()
monkey.color("Yellow")
monkey.shape("Turtle")

while True:
    x = mcb.accelerometer.get_x()
    print(x)

    if x > 300:
        print("Right!")
        laura.forward(5)
    
    if x < -300:
        print("LEFT!")
        laura.backward(5)
