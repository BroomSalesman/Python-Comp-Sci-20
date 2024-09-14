import turtle as tur

canvas = tur.Screen()
canvas.bgcolor("Yellow")
tur = tur.Turtle()
tur.pensize(3)
tur.color("Lime")

for i in range (5):
    tur.forward(200)
    tur.left(360/5)