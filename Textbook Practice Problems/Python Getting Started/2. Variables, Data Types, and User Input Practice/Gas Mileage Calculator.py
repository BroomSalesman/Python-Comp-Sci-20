# Gas Mileage Calculator
# Labeeb Farooqi
# April 11, 2023

# User enters kilometres driven and litres of gasoline used
kilometers_driven = float(input("\n\n\n\nEnter the number of kilometers driven:\n"))
litres_used = float(input("\nEnter the amount of gasoline used in litres.\n"))

# Calculates litres per 100 kilometers (L/100km)
kilometers_driven = (kilometers_driven/kilometers_driven) * 100
litres_used = (litres_used/kilometers_driven) * 100

# Outputs the rate of litres per 100 kilometer.add()
print(f"\n\nThe calculated rate of gas usage is {litres_used}/{kilometers_driven}\n\n\n\n\n\n")
