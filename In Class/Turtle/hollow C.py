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

# Back start point (bottom left outer line), draws bottom outer line
turt.goto(0, -100)
turt.right(90)
turt.pendown()
turt.forward(200)
turt.penup()

# Goes back to
turt.goto(0, 100)
turt.pendown()
turt.forward(200)
turt.penup()

# Done outer perimeter at this point (big C)

turt.goto(100, -100)
turt.right(90)
turt.pendown()
turt.forward(40)
turt.penup()

turt.goto(100, 100)
turt.right(180)
turt.pendown()
turt.forward(40)
turt.penup()


turt.goto(100, -60)
turt.right(90)
turt.pendown()
turt.forward(160)
turt.penup()

turt.goto(100, 160)
turt.pendown()
turt.forward


