#########################################################
# Labeeb Farooqi
# Computer Science 20
# March 27, 2023
#
# Temperature Conversion Program
# Purpose: To convert a temperature from celsius to fahrenheit.
#################################################################

#      All possible conversions        #

import time


#Defines all possible input options
possible_temp_units = ["C", "F", "K"]

def show_options():
    """Prints out text"""    
    print("\nEnter C for Celsius.")
    print("\nEnter F for Fahrenheit")
    print("\nEnter K for Kelvin")

#Program startup
for dot in range(3):
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\nInitializing.")
time.sleep(0.3333)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\nInitalizing..")
time.sleep(0.3333)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\nInitalizing...")
time.sleep(0.3333)

time.sleep(3)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nThis program, written by Labeeb Farooqi, is designed to convert one unit of temperature to another."
         "To use it, you must enter what unit you want to convert from (), what unit you would like to" 
         "\nconvert to, and then enter the temperature to be calculated (which must be a number)")

# Prompts user to input the unit of temperature they want to convert from.
time.sleep(5)
print("\n\nWhat temperature unit would you like to convert from?")
time.sleep(2)
show_options()
time.sleep(1.5)
temp_unit_from = input("\nEnter your selection:  ").upper()




# If input is not C, F, or K, user will be prompted for input again.
if not temp_unit_from in possible_temp_units:
    print("\n\nThat is not an option")
    time.sleep(1.5)
    show_options()
    time.sleep(1.5)
    temp_unit_from = input("\nRenter your selection:  ").upper()

if temp_unit_from == "C":
    time.sleep(1.25)
    temp_unit_from_word = "Celsius"
    print(f"\n\nYou chose {temp_unit_from }.")

elif temp_unit_from == "F":
    time.sleep(1.25)
    temp_unit_from_word = "Fahrenheit"
    print(f"\n\nYou chose  {temp_unit_from}.")
else:
    time.sleep(1.25)
    temp_unit_from_word = "Kelvin"
    print(f"\n\nYou chose {temp_unit_from}.")
    

# Prompts user to input the unit of temperature they want to convert to.
time.sleep(0.65)
print("\n\nWhat unit of temperature would you like to convert to?")
show_options()
temp_unit_to = input("\nEnter your selection:  ").upper()



# If input is not C, F, or K, user will be prompted for input again.
if not temp_unit_from in possible_temp_units:
    print("\n\nThat is not an option")
    time.sleep(1.5)
    show_options()
    time.sleep(1.5)
    temp_unit_from = input("\nRenter your selection:  ").upper()
    
if temp_unit_to == "C":
    time.sleep(1.25)
    temp_unit_to_word = "Celsius"
    print(f"\nYou chose {temp_unit_to}.")

elif temp_unit_to == "F":
    time.sleep(1.25)
    temp_unit_to_word = "Fahrenheit"
    print(f"\nYou chose {temp_unit_to}.")

else:
    time.sleep(1.25)
    temp_unit_to = "Kelvin"
    print(f"\nYou chose {temp_unit_to}.")

temp = float(input("\n\nEnter temperature (should be a number):"))

while not type(temp) == float or type(temp) == int: #checking 
    time.sleep(0.5)
    print("\nThat is not a valid number. Make sure there is nothing but numbers in your response.")
    user_temp = float(input("\n\nEnter temperature (should be a number):"))



# Celsius to Fahrenheit
if temp_unit_from == "C" and temp_unit_to == "F":
    conversion = (temp * 1.8) + 32

# Celsius to Kelvin
elif temp_unit_from == "C" and temp_unit_to == "K":
    conversion = temp + 273.15

# Fahrenheit to Celsius
elif temp_unit_from == "F" and temp_unit_to == "C":
    conversion = (temp - 32) / 1.8

# Fahrenheit to Kelvin
elif temp_unit_from == "F" and temp_unit_to == "K":
    conversion = (temp + 459.67) * 5/9

# Kelvin to Celsius
elif temp_unit_from == "K" and temp_unit_to == "C":
    conversion = temp - 273.15

# Kelvin to Fahrenheit
elif temp_unit_from == "K" and temp_unit_to == "F":
    conversion = (temp * 1.8) - 459.67 

print("Calculating. This may take some time.")
time.sleep(5)
print(f"Pay $({conversion}) CAD to view results.")


    

