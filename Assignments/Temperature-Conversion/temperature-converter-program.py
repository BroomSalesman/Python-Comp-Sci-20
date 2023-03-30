#########################################################
# Labeeb Farooqi
# Computer Science 20
# March 27, 2023
#
# Temperature Conversion Program
# Purpose: To convert a temperature from celsius to fahrenheit.
#################################################################

#      All possible conversions        #

def show_options():
    print("\nEnter C for Celsius.")
    print("\nEnter F for Fahrenheit")
    print("\nEnter K for Kelvin")

#Defines all possible input options
possible_temp_units = ["C", "F", "K"]

# Prompts user for unit of temperature they want to convert from.
print("\n\n\n\nWhat temperature unit would you like to convert from?")
show_options()
temp_unit_to_convert_from = input("\nEnter your selection:  ").upper()

# If input is not C, F, or K, user will be prompted for input again.
if not temp_unit_to_convert_from in possible_temp_units:
    print("\n\nThat is not an option")
    show_options()
    temp_unit_to_convert_from = input("\nEnter your selection:  ").upper() # type: ignore

if temp_unit_to_convert_from == "C":
    temp_unit_to_convert_from = "Celsius"
    print("\nYou chose " + temp_unit_to_convert_from + ".")

elif temp_unit_to_convert_from == "F":
    temp_unit_to_convert_from = "Fahrenheit"
    print("\n\nYou chose " + temp_unit_to_convert_from + ".")
    
else:
    temp_unit_to_convert_from = "Kelvin"
    print("\nYou chose " + temp_unit_to_convert_from + ".")

# Prompts user to 
print("What unit of temperature would you like to convert to?")
show_options()
temp_unit_to_convert_to = input("\nEnter your selection:  ")

