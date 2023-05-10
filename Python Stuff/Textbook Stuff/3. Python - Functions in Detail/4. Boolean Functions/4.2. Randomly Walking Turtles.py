import turtle
import random

def is_on_screen(window, a_turtle):
    left_edge = -(window.window_width()/2)
    right_edge = window.window_width()/2 
    top_edge = window.window_height()/2
    bottom_edge = -(window.window_height()/2)
    
    x = a_turtle.xcor()
    y = a_turtle.ycor()
    
    if x > left_edge and x <  right_edge and y < top_edge and y >  bottom_edge:
        return True
    else:
        return False

canvas = turtle.Screen()
canvas.bgcolor("Dark Grey")

bob = turtle.Turtle()
bob.shape("turtle")
bob.color("yellow")
bob.pensize(5)



while is_on_screen(canvas, bob):
    choice = random.randrange(0, 3)
    if choice == 0: #forward
        bob.forward(50)
    elif choice == 1:  #left
        bob.left(90)
        bob.forward(50)
    else: #right
        bob.right(90)
        bob.forward(50)
        
print("All done!")