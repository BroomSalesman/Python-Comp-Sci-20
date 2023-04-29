
import turtle

def draw_square(my_turtle, side_length):
    """ my_turtle -> turtle.Turtle() object
         side_length -> integer or float
         
         Draws a square according to side_length"""
    for side in range(4):
        my_turtle.right(90)
        my_turtle.forward(side_length)

def draw_square_logo(my_turtle, side_length):
    """Draws a square with a diamond in it (which is just a square but rotated at an angle). You'll see what it is. 

    Args:
        my_turtle (turtle.Turtle() object): Draws the squares using turtle module.
        side_length (int, float): Determines side lengths of both squares.
    """
    draw_square(my_turtle, side_length)
    my_turtle.penup()
    my_turtle.backward(side_length/2)
    my_turtle.right(90)
    my_turtle.forward(side_length/2)
    my_turtle.left(45)
    my_turtle.pendown()
    draw_square(my_turtle, side_length)


canvas = turtle.Screen()
canvas.bgcolor("dark gray")

bob = turtle.Turtle()
bob.shape("turtle")
bob.color("hot pink")
bob.pensize(5)

draw_square_logo(bob, 50)

