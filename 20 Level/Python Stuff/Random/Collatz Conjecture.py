try:
    number = input("\n\n\nEnter a POSITIVE WHOLE number:")
    x = int(number)
    assert isinstance(x, int) and x > 0
except (ValueError, AssertionError):
    raise ValueError("\n\nInvalid number. Number has to be a whole number above 0.\n")

nums = []
nums.append(x)
if x % 2 == 0:
    print("\n" + str(x) + " is even, so it will be divided by 2.\n")
else:
    print("\n" + str(x) + " is odd, so it will be multiplied by 3 and then increased by 1 (3x + 1).\n")

# Loop starts running as long as x is not 4.
while x > 4 or x == 4:
    if x%2 == 0:
        x = int(x/2)
        print(x)
    else:
        x = 3*x + 1
        print(x)

    nums.append(x)

    if x % 2 == 0:
        print("\n" + str(x) + " is even, so it will be divided by 2.\n")
    else:
        print("\n" + str(x) + " is odd, so it will be multiplied by 3 then increased by 1 (3x + 1).\n")

nums.append(2)
nums.append(1)

for i in range(3):
    for i in range(3):
        if x%2 == 0:
            x = int(x/2)
            print(x)
        else:
            x = 3*x + 1
            print(x)
        if x % 2 == 0:
            print("\n" + str(x) + " is even, so it will be divided by 2.\n")
        else:
            print("\n" + str(x) + " is odd, so it will be multiplied by 3 then increased by 1 (3x + 1).\n")

print("As you can see, the number is stuck in a loop now. This is what makes Collatz conjecture so famous.\n No matter what number you choose, it will always lead to this.")

print("\n" + str(nums)+ "\n\n")

print(f"The highest number you reached was: {max(nums)}")
print

