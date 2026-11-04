# Labeeb Farooqi
# HPO267
# 11432366

def combined_wall_area(w, h):
    """Calculates the combined area of four dimensionally equal walls and returns a float or int"""
    return w*h*4

def calculate_roof_area(w, s):
    """Calculates the surface area of four-sided pyramid shaped roof and returns a float or int"""
    return (w*s/2) * 4

def house_paint_cost(w, h, s, paint_cost):
    """Calculates and return the total cost to paint the walls and roof of a house based on the dimensions of its walls and roof

        Parameters:
            w (float or int: width of the walls and base of the pyramid shaped roof
            h (float or int): height of the walls
            s (float or int): slant height of the roof
            paint_cost (float or int): cost per square metre of paint

        Returns:
            float: Total cost of the trip rounded to 2 decimal places if necessary, rounded to decimal places if necessary
    """

    # Calculates and adds up the areas of the walls and roof
    house_surface_area = combined_wall_area(w, h) + calculate_roof_area(w, s)

    # Calculates total cost of paint needed is a float with at most 2 decimal places
    return round(float(house_surface_area * paint_cost), 2)


print("House Exterior Paint Cost Calculator:")

# Collects user input to be used as parameters for the house_paint_cost() function
user_width = float(input("Enter the shared width of house walls and base of the roof: "))
user_height = float(input("Enter height of house walls: "))
user_slant = float(input("Enter roof slant height: "))
user_paint_cost = float(input("Enter cost per square metre of paint ($): "))

print("The total cost of paint needed to paint the exterior of the house is $" + str(house_paint_cost(user_width, user_height, user_slant, user_paint_cost)))

