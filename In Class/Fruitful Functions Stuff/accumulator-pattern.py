def square(number):
    # initialize
    total = 0

    # repeat
    for counter in range(number):
        # modify
        total = total + number

    return total


print(square(5))


def accumulator_sum(number):
    # initialize
    sum = 0

    # repeat
    for counter in range(number + 1):
        # modify
        sum = number + counter

    return sum