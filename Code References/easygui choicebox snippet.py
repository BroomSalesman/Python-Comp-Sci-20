import easygui

# Define a list of numbers
banana = []
for i in range(81):
    banana.append(i+20)

# Use choicebox to display the numbers and allow the user to choose one
selected_number = easygui.choicebox("Please select a number", "Number selection", banana)

# Print the selected number to the console
print(f"You selected {selected_number}")