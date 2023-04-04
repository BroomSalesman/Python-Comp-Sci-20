import turtle as tur

window = tur.Screen()
window.bgcolor("lightyellow")

turt = tur.Turtle()
turt.shape("Turtle")
turt.color("hotpink")
turt.pensize(4)
turt.penup()
turt.speed(0)

for side in range(2, 100):
    turt.stamp()