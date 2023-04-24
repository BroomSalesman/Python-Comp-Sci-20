def rectangle_area(length, width):
    area = length * width
    
    return area

assert rectangle_area(5, 10) == 50
assert rectangle_area(1, 10) == 10
assert rectangle_area(2, 6) == 12
assert rectangle_area(1, 1) == 1
assert rectangle_area(3, 5) == 15
assert rectangle_area(15, 4) == 60

print("Code passed all assertions, so it is correct.")
