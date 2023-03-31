import turtle
import microbit as mcb

while True:
    x = mcb.accelerometer.get_x()
    print(x)