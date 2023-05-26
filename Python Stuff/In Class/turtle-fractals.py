import turtle

def apply_rules(letter):
    if letter == "A":
        return "B"

    elif letter == "B":
        return "AB"

    else:
        return letter

def process_string(some_string):
    transformed_string = ""
    for letter in some_string:
        transformed_string = transformed_string + apply_rules(letter)

    return transformed_string

def create_l_system(iterations, axiom):
     new_string = axiom
     for counter
















"""
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
"""
