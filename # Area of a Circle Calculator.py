# Area of a Circle Calculator
# Labeeb Farooqi
#2023-03-17
import turtle as turtle
import math

diameter = input("Enter the diameter of the circle.\nIf you know the radius, press enter and then enter the radius.\n")
if diameter == "":
    radius = float(input("\nEnter the radius of the circle."))
else:
    radius = float(diameter)/2

area = math.pi*radius**2

print("The area of the circle is: ", area)

turtle.pendown()
turtle.circle(radius)
turtle.done()
print("Task Executed Successfully")