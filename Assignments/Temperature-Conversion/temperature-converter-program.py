#########################################################
# Labeeb Farooqi
# Computer Science 20
# March 27, 2023
#
# Temperature Conversion Program
# Purpose: To convert a temperature from celsius to fahrenheit.
#################################################################

#      All possible conversions        #

def show_first_options():
    print("Enter C for Celsius.")
    print("\nEnter F for Fahrenheit")
    print("\nEnter K for Kelvin")

#Defines all possible input options
possible_temp_units = ["C", "F", "K"]

print
temp_unit_to_convert_from = input("\nEnter your selection:  ").upper()

# If input is not C, F, or K, user will have to enter again.
if not temp_unit_to_convert_from in possible_temp_units:
    print("That is not an option")
    show_first_options()
    temp_unit_to_convert_from = input("\nEnter your seleection:  ").upper() # type: ignore

if temp_unit_to_convert_from == "C":
    temp_unit_to_convert_from = "Celsius"
    print("You chose " + temp_unit_to_convert_from + ".")

elif temp_unit_to_convert_from == "F":
    temp_unit_to_convert_from = "Fahrenheit"
    print("You chose " + temp_unit_to_convert_from + ".")
    
else:
    temp_unit_to_convert_from = "Kelvin"
    print("You chose " + temp_unit_to_convert_from + ".")

temp_unit_to_convert_to = input("What unit of temperature would you like to convert to?")


