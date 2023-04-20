# Area of a Rectangle Calculator
# Labeeb Farooqi
# April 11, 2023

print("This program is designed to calculate the area of a rectangle.")

# User inputs length and width of rectangle
length = float(input("\nEnter the length of the rectangle.\n"))
width = float(input("\nEnter the width of the rectangle.\n"))
unit = input("\nEnter unit of measurement (it can also be any random word, it wont correct you if you write cats instead of centimeter.)\n")


# Calculates and prints the area of the rectangle in one line of code
print(f"\nThe area of the rectangle is {length * width} {unit}\u00B2.")