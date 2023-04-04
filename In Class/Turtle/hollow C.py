import turtle


screen = turtle.Screen()
screen.bgcolor("Dark Grey")

turt = turtle.Turtle()
turt.pensize(3)
turt.color("hotpink")

turt.speed(3)

# Goes to bottom left corner (the left outer line)
turt.penup()
turt.goto(0, -100)

# Draws upwards, left outer line
turt.left(90)
turt.pendown()
turt.forward(200)
turt.penup()

# Back start point (bottom of left outer line), draws bottom outer line
turt.goto(0, -100)
turt.right(90)
turt.pendown()
turt.forward(200)
turt.penup()

# Goes to top of left outer line, draws top outer line
turt.goto(0, 100)
turt.pendown()
turt.forward(200)
turt.penup()

# Done normal C shape (should look like square with no right side)

# Goes to bottom right point (of bottom outer line), then draws farthest right line (one of the small lines)
turt.goto(200, -100)
turt.left(90)
turt.pendown()
turt.forward(40)
turt.penup()

# Does the same as above, but at the top
turt.goto(200, 100)
turt.right(180)
turt.pendown()
turt.forward(40)
turt.penup()

# Goes to bottom short line, and draws bottom inside line
turt.goto(200, -60)
turt.right(90)
turt.pendown()
turt.forward(160)
turt.penup()

# Same as above, but for upper inside line
turt.goto(200, 60)
turt.pendown()
turt.forward(160)
turt.penup()

