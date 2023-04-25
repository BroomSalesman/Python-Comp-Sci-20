def find_min(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    elif c < a and c < b:
        return c
    else:
        return a















assert find_min(4, 7, 5) == 4
assert find_min(4, 5, 5) == 4
assert find_min(4, 4, 4) == 4
assert find_min(2, -6, -100) == -100
assert find_min(-2, -100, 6) == -100
assert find_min(4, -7, 5) == -7
assert find_min(-4, 7,  -5) == -5

print("\n\n\n\nAll assertions passed. Function works as intended.")