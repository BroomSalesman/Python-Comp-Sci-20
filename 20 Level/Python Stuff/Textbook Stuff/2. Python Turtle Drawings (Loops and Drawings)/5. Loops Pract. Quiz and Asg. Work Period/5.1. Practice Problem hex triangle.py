import turtle

canvas  = turtle.Screen()
canvas.bgcolor("Dark Gray")


bob = turtle.Turtle()
bob.color("Lime")
bob.pensize(5)
bob.shape("turtle")


def draw_triangle(some_turtle, side_length):
    """Draws an equaliteral triangle using turtle module

    Args:
        some_turtle (turtle.Turtle()): Turtle used to draw
        side_length (int, float): Must be a valid number
    """
    for i in range (3):
        some_turtle.forward(side_length)
        some_turtle.left(120)
    
for triangle in range(6):
        draw_triangle(bob, 100)
        bob.left(60)