#################################################################
# Labeeb Farooqi
# Computer Science 20
# April 11, 2023
#
# Mad Lib Program
# Purpose: To create a mad lib through user input and random selection
################################################################

import time


print("\n\n\n\n\n\n\n  In case you don't know what a madlib is, press N and ENTER.\n If you do know what a mad lib is, only press ENTER")

continue1 = input("")

# The comment below is just to show you what I was originally going to do. I mean it's nothing big, but it's something, eh?
# if len(continue1) > 0:
#     continue1 = continue1.upper()

if continue1 == "N":
    print("\n\nA madib is a game/interactive-story that takes words from the player/reader to fill in little gaps in the story.")
    print("The blanks usually have a little word below them, to determine what the word should be. The basic specifications are nouns, adjectives, verbs, adverbs, names, etc.,")
    print("but there are also more specific blanks, such as 'a type of food', 'something that flies', 'a country', etc.")
    print("You will not get to see the madlib before choosing words first for this madlib.")
    
time.sleep(5)

print("\nYou have 3 different types of madlibs to choose from:")
time.sleep(0.5)
print("1. A madlib in which you choose all the words.")
time.sleep(0.25)
print("2. A madlib in which you choose half of the words and the rest are randomly generated.")
time.sleep(0.25)
print("A madlib in which all the words are computer generated.")



