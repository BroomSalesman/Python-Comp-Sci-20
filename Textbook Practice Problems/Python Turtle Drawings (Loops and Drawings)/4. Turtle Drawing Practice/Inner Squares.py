import turtle

window = turtle.Screen()
window.bgcolor("Dark Gray")

bob = turtle.Turtle()
bob.shape("turtle")

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
        inner_side_length (integer, float): 
        buffer_length (float, integer): _description_
    """     

draw_square(bob, 21)
    

        
        
        
