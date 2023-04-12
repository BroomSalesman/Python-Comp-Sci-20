#########################################################
# Labeeb Farooqi
# Computer Science 20
# March 27, 2023
#
# Temperature Conversion Program
# Purpose: To convert a temperature from celsius to fahrenheit.


# There are 3 key parts to this, all that are determined by input from user:
#       Part 1: Unit of temperature to convert FROM. Example: CELSIUS to Fahrenheit (Celsius is the unit of temperature to convert from) 
#       Part 2: Unit of temperature to convert TO. Example:  Celsius to FAHRENHEIT (Fahrenheit is the unit to convert to)
#       Part 3: The ACTUAL TEMPERATURE NUMBER that will be converted to another unit of temperature. Example: 12 °C to Fahrenheit (12)
# 
# The first two parts will determine what conversion formula must be used.
#  The last part, the actual temperature, will be plugged into the formula and then returned  
#################################################################


# Time module will be used to create delays
import time

#Defines all possible input options, 
possible_temp_units = ["C", "F", "K"]

# Function to show user what to input their temperature unit as
def show_options():
    print("\nEnter C for Celsius.")
    print("\nEnter F for Fahrenheit")
    print("\nEnter K for Kelvin")



 # For loop used to create a loading effect
for dot in range(4):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\nInitializing.")
    time.sleep(0.20)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\nInitalizing..")
    time.sleep(0.2)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\nInitalizing...")
    time.sleep(0.2)

# Prints introduction to program and how to use it
time.sleep(0.5)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nThis program, written by Labeeb Farooqi, is designed to convert one unit of temperature to another."
         "  To use it, you must enter what unit you want to convert from (), what unit you would like to" 
         "\nconvert to, and then enter the temperature to be calculated (which must be a number).")
time.sleep(2)

# Next line of code is executed only after users presses enter
input("\nPress enter if you have finished reading.")



######  Part 1: Asks user to input unit of temperature to convert FROM ######

time.sleep(1)
print("\nWhat temperature unit would you like to convert from? Example: CELSIUS to fahrenheit")
time.sleep(1.5)
show_options()
time.sleep(2)
temp_unit_from = input("\nEnter your selection:  ").upper()




# Checks if user entered valid option
if not temp_unit_from in possible_temp_units:
    print("\n\nThat is not an option")
    time.sleep(1.5)
    show_options()
    time.sleep(1.5)
    temp_unit_from = input("\nRenter your selection:  ").upper()


# Creates word version of temperature unit for outputting string purposes,
if temp_unit_from == "C":
    time.sleep(1.25)
    temp_unit_from_word = "Celsius"
    print(f"\n\nYou chose {temp_unit_from_word}.")

elif temp_unit_from == "F":
    time.sleep(1.25)
    temp_unit_from_word = "Fahrenheit"
    print(f"\n\nYou chose  {temp_unit_from_word}.")

else:
    time.sleep(1.25)
    temp_unit_from_word = "Kelvin"
    print(f"\n\nYou chose {temp_unit_from_word}.")
    

# Prompts user to input the unit of temperature they want to convert to.
time.sleep(0.65)
print("\n\nWhat unit of temperature would you like to convert to? Example: Celsius to FAHRENHEIT")
show_options()
temp_unit_to = input("\nEnter your selection:  ").upper()


# If input is the same unit of temperature selected
if not temp_unit_to in possible_temp_units:
    if temp_unit_to == temp_unit_from:
        print("\n\nYou have already picked that as the first temperature unit")
        time.sleep(1.5)
        show_options()
        time.sleep(1.5)
        temp_unit_from = input("\nRenter your selection:  ").upper()
    else:
        print("")
    
    
    # User selection is stored in another 
if temp_unit_to == "C":
    time.sleep(1.25)
    temp_unit_to_word = "Celsius"
    print(f"\nYou chose {temp_unit_to_word}.")

elif temp_unit_to == "F":
    time.sleep(1.25)
    temp_unit_to_word = "Fahrenheit"
    print(f"\nYou chose {temp_unit_to_word}.")

else:
    time.sleep(1.25)
    temp_unit_to_word = "Kelvin"
    print(f"\nYou chose {temp_unit_to_word}.")

temp_to_be_converted = float(input("\n\nEnter temperature (should be a number):"))

while not type(temp_to_be_converted) == float or type(temp_to_be_converted) == int:
    time.sleep(0.5)
    print("\nThat is not a valid input. Make sure there is nothing but numbers in your response.")
    user_temp = float(input("\n\nEnter temperature (must be a number):"))



##### Calculates conversions based on user selections #######
# Celsius to Fahrenheit
if temp_unit_from == "C" and temp_unit_to == "F":
    converted_temperature = (temp_to_be_converted * 1.8) + 32

# Celsius to Kelvin
elif temp_unit_from == "C" and temp_unit_to == "K":
    converted_temperature = temp_to_be_converted + 273.15

# Fahrenheit to Celsius
elif temp_unit_from == "F" and temp_unit_to == "C":
    converted_temperature = (temp_to_be_converted - 32) / 1.8

# Fahrenheit to Kelvin
elif temp_unit_from == "F" and temp_unit_to == "K":
    converted_temperature = (temp_to_be_converted + 459.67) * 5/9

# Kelvin to Celsius
elif temp_unit_from == "K" and temp_unit_to == "C":
    converted_temperature = temp_to_be_converted - 273.15

# Kelvin to Fahrenheit
elif temp_unit_from == "K" and temp_unit_to == "F":
    converted_temperature = (temp_to_be_converted * 1.8) - 459.67 





######## Prints the converted temperature ######### 
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\nCalculating. This may take some time.")
time.sleep(8)

#Since Kelvin does not have degrees before it, a boolean must be used to not include the degree symbol if Kelvin is either the .
if temp_unit_from == "K":
    print(f"\n{temp_to_be_converted} K is {converted_temperature} \u00b0{temp_unit_to}\n\n\n")
    
elif temp_unit_to == "K":
    print(f"\n{temp_to_be_converted} \u00b0{temp_unit_from} is {converted_temperature} K.\n\n\n")
    
elif temp_unit_from == "K" and temp_unit_to == "K":
    print(f"\n{temp_to_be_converted} K is {converted_temperature} K.\n\n\n") # Remove this later
    
else:
    print(f"\n{temp_to_be_converted} \u00b0{temp_unit_from} is {converted_temperature} \u00b0{temp_unit_to}.\n\n\n")
    

