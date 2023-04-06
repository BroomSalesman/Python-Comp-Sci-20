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

def show_options():
    print("\nEnter C for Celsius.")
    print("\nEnter F for Fahrenheit")
    print("\nEnter K for Kelvin")

#Defines all possible input options
possible_temp_units = ["C", "F", "K"]

def show_options():
    print("\nEnter C for Celsius.")
    print("\nEnter F for Fahrenheit")
    print("\nEnter K for Kelvin")

#Program startup
print("Initializing...")
time.sleep(3)
print("This program, written by Labeeb Farooqi, is designed to convert one unit of temperature to another.\n")
print("To use it, you must enter what unit you want to convert from (), what unit you would like to convert to,\n and then enter the temperature to be calculated (which must be a number)")



# Prompts user to input the unit of temperature they want to convert from.
time.sleep(5)
print("\n\n\n\nWhat temperature unit would you like to convert from?")
time.sleep(2)
show_options()
time.sleep(1.5)
temp_unit_to_convert_from = input("\n\nEnter your selection:  ").upper()




# If input is not C, F, or K, user will be prompted for input again.
if not temp_unit_to_convert_from in possible_temp_units:
    print("\n\nThat is not an option")
    time.sleep(1.5)
    show_options()
    time.sleep(1.5)
    temp_unit_to_convert_from = input("\nRenter your selection:  ").upper()

if temp_unit_to_convert_from == "C":
    time.sleep(1.25)
    temp_unit_to_convert_from = "Celsius"
    print("\n\nYou chose " + temp_unit_to_convert_from + ".")

elif temp_unit_to_convert_from == "F":
    time.sleep(1.25)
    temp_unit_to_convert_from = "Fahrenheit"
    print("\n\nYou chose " + temp_unit_to_convert_from + ".")
    
else:
    time.sleep(1.25)
    temp_unit_to_convert_from = "Kelvin"
    print("\n\nYou chose " + temp_unit_to_convert_from + ".")
    

# Prompts user to input the unit of temperature they want to convert to.
time.sleep(0.65)
print("\n\nWhat unit of temperature would you like to convert to?")
show_options()
temp_unit_to_convert_to = input("\nEnter your selection:  ").upper()



# If input is not C, F, or K, user will be prompted for input again.
if not temp_unit_to_convert_from in possible_temp_units:
    print("\n\nThat is not an option")
    time.sleep(1.5)
    show_options()
    time.sleep(1.5)
    temp_unit_to_convert_from = input("\nRenter your selection:  ").upper()
    
if temp_unit_to_convert_to == "C":
    time.sleep(1.25)
    temp_unit_to_convert_to = "Celsius"
    print("\nYou chose " + temp_unit_to_convert_to + ".")

elif temp_unit_to_convert_to == "F":
    time.sleep(1.25)
    temp_unit_to_convert_to = "Fahrenheit"
    print("\nYou chose " + temp_unit_to_convert_to + ".")

else:
    time.sleep(1.25)
    temp_unit_to_convert_to = "Kelvin"
    print("\nYou chose " + temp_unit_to_convert_to + ".")

user_temp = float(input("\n\nEnter temperature (should be a number)):"))

while not type(user_temp) == float or type(user_temp) == int: #checking for integer is there  
    print("\nThat is not a valid number. Make sure there are no letters or special characters in your input.")
    

