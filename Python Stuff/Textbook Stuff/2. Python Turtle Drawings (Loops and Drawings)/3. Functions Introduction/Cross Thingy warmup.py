import turtle

window = turtle.Screen()
window.bgcolor("Gray")

bob = turtle.Turtle()
bob.shape("turtle")
bob.color("Pink")

for line in range(4):
    bob.right(90)
    bob.forward(50)
    bob.left(90)
    bob.forward(50)
    bob.right(90)
    bob.forward(50)