import random

def get_average(numbers: list):
    return sum(numbers)/len(numbers)

random_nums = [random.randrange(0, 1000) for i in range(100)]

print(random_nums)
print("\n\nAverage:")
print(get_average(random_nums))
