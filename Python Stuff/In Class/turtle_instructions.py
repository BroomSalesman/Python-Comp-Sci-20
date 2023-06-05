import turtle

canvas = turtle.Screen()
canvas.bgcolor("Black")

king_bob = turtle.Turtle()
king_bob.color("light blue")
king_bob.pensize(5)
king_bob.shape("turtle")

instructions = "F-F++F-F"

for task in instructions:
    if task == "F":
        king_bob.forward(25)
    elif task == "+":
        king_bob.right(45)
    elif task == "-":
        king_bob.left(45)
