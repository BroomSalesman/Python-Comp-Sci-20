import turtle

def draw_square(my_turtle, side_length):
    """ my_turtle -> turtle.Turtle() object
         side_length -> integer or float
         
         Draws a square according to side_length"""
    for line in range(4):
        my_turtle.forward(side_length)
        my_turtle.right(90)
   
   
   
        
def draw_inner_square(some_turtle, inner_side_length, buffer_length):
    """Draws a square with a smaller square inside of it

    Args:
        some_turtle (turtle.Turtle() object): Uses a turtle.Turtle() object to draw
        inner_side_length (integer, float): The side length of the inner square  
        buffer_length (float, integer): Determines how far away to draw the outer square from the inner square and the side length of the outer square.
    """ 
    draw_square(some_turtle, inner_side_length)
    some_turtle.penup()
    some_turtle.backward(buffer_length)
    some_turtle.right(90)
    some_turtle.forward(buffer_length)
    some_turtle.left(90)
    some_turtle.pendown()
    draw_square(some_turtle, inner_side_length + buffer_length*2)

    

window = turtle.Screen()
window.bgcolor("Dark Gray")

bob = turtle.Turtle()
bob.shape("turtle")
bob.pensize(7)
bob.color("Hot Pink")

draw_inner_square(bob, 50, 3.5)
        
        
        
