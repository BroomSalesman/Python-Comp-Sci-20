# This entrypoint file to be used in development. Start by reading README.md
# In your command prompt or powershell, use the command 'pip install pytest' for the pytest module to work.
from pytest import main

from arithmetic_arranger import arithmetic_arranger

print("Example:")
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

print("\n\n")

print("Tests:")
# Output without solution for the arithmetic problem
print(arithmetic_arranger(['3801 - 2', '123 + 49']))
print("\n")
print(arithmetic_arranger(['1 + 2', '1 - 9380']))
print("\n")
print(arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49']))
print("\n")
print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']))
print("\n")

# Output testing restrictive/foolproof errors
print(arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49','888 + 40', '653 + 87']))
print("\n")
print(arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49']))
print("\n")
print(arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']))
print("\n")
print(arithmetic_arranger(['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']))
print("\n")

# Output with solution shown below arithmetic problem
print(arithmetic_arranger(['3 + 855', '988 + 40'], True))
print("\n")
print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))
print("\n")


# Run unit tests automatically
main(['-vv'])
