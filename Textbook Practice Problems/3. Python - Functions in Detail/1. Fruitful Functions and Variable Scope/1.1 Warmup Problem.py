import turtle

def draw_rectangle(some_turtle, length, width):
    """Draws a rectangle using turtle

    Args:
        some_turtle (turtle.Turtle() object): A turtle for drawing
        length (int, float): Determines length of the rectangle
        width (int, float): Detemines width of the rectangle
    """
    
    for side in [width, length, width, length]:
        some_turtle.forward(side)
        some_turtle.left(90)

canvas = turtle.Screen()
canvas.bgcolor("dark gray")

bob = turtle.Turtle()
bob.pensize(4)
bob.color("sky blue")
bob.shape("turtle")

for rectangle in range (4):w
    draw_rectangle(bob, 50, 70)
    bob.right(90)