import turtle as tur

canvas = tur.Screen()


monkey = tur.Turtle()
monkey.shape("turtle")
monkey.color("purple")


for i in range(4):
    monkey.forward(175)
    monkey.left(90)


