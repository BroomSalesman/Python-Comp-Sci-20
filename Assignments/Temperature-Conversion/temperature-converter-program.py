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
    print("Press C to convert from celsius to another unit of temperature.")
    print("\nPress F to convert from fahrenheit to another unit of temperature.")
    print("\n Press K to convert from kelvin to another unit of temperautre.")

possible_temp_units = ["C", "F", "K"]
temp_unit_to_convert_from = input("\nEnter your selection:  ").upper()

if not temp_unit_to_convert_from in possible_temp_units:
    print("That is not an option")
    show_options()
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
