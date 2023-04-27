# pylint: disable=missing-docstring, invalid-name
def ver1_is_divisible(x, y):
    if x % y == 0:
        result = True
    else:
        result = False

    return result

print (ver1_is_divisible(10, 5))
print(ver1_is_divisible(7, 3))

def ver2_is_divisible(x, y):
    return x % y == 0

if ver2_is_divisible(10, 5):
    print("That works")

else:
    print("That doesn't work.")