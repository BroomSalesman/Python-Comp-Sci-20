try:
    x = int(input("Enter a positive integer: "))
    if x <= 0:
        raise ValueError("Number should be positive")
except ValueError as e:
    print(e)