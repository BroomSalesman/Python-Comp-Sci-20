

import turtle


def draw_cross(a_turtle, side_length):
    '''a_turtle -> turtle.Turtle() object
       side_length -> int

        Draw a cross/Swiss flag shape.'''
    for line in range(4):
        a_turtle.right(90)
        a_turtle.forward(side_length)
        a_turtle.left(90)
        a_turtle.forward(side_length)
        a_turtle.right(90)
        a_turtle.forward(side_length)


def draw_square(a_turtle, side_length):
    '''a_turtle -> turtle.Turtle() object
       side_length -> int

       Draws a square'''
    a_turtle.goto(0, 0)
    for side in range(4):
        a_turtle.forward(side_length)
        a_turtle.left(90)


window = turtle.Screen()
bob = turtle.Turtle()
bob.pensize(10)

draw_cross(bob, 50)
