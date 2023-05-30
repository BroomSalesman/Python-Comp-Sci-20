distance = float(input("Enter distance in meters"))
time = float(input("Enter time in seconds"))

mps = distance/time
mph = mps * 3600
kmph = mph / 1000
print(f"Speed is {kmph}km/h")