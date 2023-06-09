import turtle

def draw_cross(a_turtle, side_length):
    '''a_turtle -> turtle.Turtle() object
       side_length -> int
       
       Draw a cross/Swiss flag shape.'''
    for u_shape in range(4):
        for side in range(3):
            a_turtle.forward(side_length)
            a_turtle.left(90)
        a_turtle.left(180)

def draw_square(some_turtle, side_length):
    '''some_turtle -> turtle.Turtle() object
       side_length -> int
       
       Draw a square with the given turtle and side length.'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)

def draw_c(a_turtle, longest_side_length, width_of_c):
    '''a_turtle -> turtle.Turtle() object
       longest_side_length -> int
       width_of_c -> int
       
       Draws a C shape, with the gap within the C being the width_of_c.'''
    a = longest_side_length
    b = longest_side_length - width_of_c
    c = width_of_c
    d = longest_side_length - width_of_c * 2
    
    for side in [d, c, b, a, b, c, d, 0, 0, d]:
        a_turtle.forward(side)
        a_turtle.left(90)

window = turtle.Screen()
victor = turtle.Turtle()
victor.pensize(5)
ieva = turtle.Turtle()
ieva.color("pink")
ieva.pensize(5)

draw_c(ieva, 200, 75)

#schellenberg's solution
# for u_shape in range(4):
#     for side in range(3):
#         victor.forward(100)
#         victor.left(90)
#     victor.left(180)

#maurya's solution
# for side in [50, 50, 50, -50, 0, 0, 50, 50, -50, 0, 0, 50, 50, -50, 0, 0, 50, 50]:
#     victor.forward(side)
#     victor.left(90)

#dhanush's solution
# for x in range(4):
#     victor.forward(100)
#     victor.left(90)
#     victor.forward(100)
#     victor.right(90)
#     victor.forward(100)
#     victor.right(90)

# hyder's solution
# for side in range(4):
#     for size in range(2):
#         victor.forward(100)
#         victor.right(90)
#     victor.forward(100)
#     victor.left(90)
