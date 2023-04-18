import easygui 

# Define a list of numbers
mainscale = []
for i in range(81):
    mainscale.append(i+20)

# Use choicebox to display the numbers and allow the user to choose one
selected_number = easygui.choicebox("Please select a number", "Number selection", mainscale)

# Print the selected number to the console
print(f"You selected {selected_number}")