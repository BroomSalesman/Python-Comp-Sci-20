import turtle as tur

canvas = tur.Screen()


monkey = tur.Turtle()
monkey.shape("turtle")
monkey.color("purple")
monkey.pensize(100)


for i in range(4):
    monkey.forward(10000)
    monkey.left(90)