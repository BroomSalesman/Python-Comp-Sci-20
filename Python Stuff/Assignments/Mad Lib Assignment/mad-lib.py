#################################################################
# Labeeb Farooqi
# Computer Science 20
# April 11, 2023
#
# Mad Lib Program
# Purpose: To create a mad lib through user input and random selection
################################################################

import time
import random

with open("adjective.txt", "r", encoding = "utf-8") as file:
    adjectives = file.readlines()
adjectives = [line.strip() for line in adjectives]

with open("adverbs.txt", "r", encoding = "utf-8") as file:
    adverbs = file.readlines()
adverbs = [line.strip() for line in adverbs]

with open('nouns.txt', 'r', encoding = 'utf-8') as file:
    nouns = file.readlines()
nouns = [line.strip() for line in nouns]

with open('verbs.txt', 'r', encoding = 'utf-8') as file:
    verbs = file.readlines()
verbs = [line.strip() for line in verbs]

with open('verb-ing.txt', 'r', encoding = 'utf-8') as file:
    verb_ing = file.readlines()
verb_ing = [line.strip() for line in verb_ing]

with open('countries.txt', 'r', encoding = 'utf-8') as file:
    countries = file.readlines()
countries = [line.strip() for line in countries]

with open('places.txt', 'r', encoding = 'utf-8') as file:
    places = file.readlines()
places = [line.strip() for line in places]

with open('plural-nouns.txt', 'r', encoding = 'utf-8') as file:
    plural_nouns = file.readlines()
plural_nouns = [line.strip() for line in plural_nouns]




 # For loop used to create a loading effect
for dot in range(4):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\nInitializing.")
    time.sleep(0.3)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\nInitalizing..")
    time.sleep(0.3)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\nInitalizing...")
    time.sleep(0.3)

print("\n\n\n\n\n\n\n  In case you don't know what a madlib is, press N and ENTER.\n If you do know what a mad lib is, only press ENTER")
time.sleep(0.5)
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

print("\nYou have 3 different types of madlibs to choose from:\n")
time.sleep(0.5)
print("1. A madlib in which you choose all the words.")
time.sleep(0.25)
print("2. A madlib in which you choose half of the words and the rest are randomly generated.")
time.sleep(0.25)
print("3. A madlib in which all the words are computer generated.\n")

time.sleep(4)


possible_selections = [1, 2, 3]
time.sleep(0.5)

while True:
    try:
        choose_madlib = int(input("To select one, press 1, 2, or 3, then press enter (see above)."))
        if choose_madlib not in possible_selections:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Try again.")
        time.sleep(0.5)
        continue

if choose_madlib == 1:
    blank1 = input("Enter a verb:  ")
    blank2 = input("Type of feeling:  ")
    blank3 = input("Adjective:  ")
    blank4 = input("Adjective:  ")
    blank5 = input("Noun:  ")
    blank6 = input("Flavor:  ")
    blank7 = input("Type of food:  ")
    blank8 = input("Something you (or other people) read:  ")
    blank9 = input("Adjective:  ")
    blank10 = input("Type of monster:  ")

    print("Standby...")
    time.sleep(5)

    print(f"Do not \033[1m{blank1}\033[0m to me before I have had my coffee!")
    print(f"Before I get my first sip, I am \033[1m{blank2}\033[0m.")
    print("If I do not get to practice my morning routine, then the day")
    print(f"is sure to be \033[1m{blank3}\033[0m. First I get \033[1m{blank4} {blank5}\033[0m mug.")
    print(f"Then I brew some \033[1m{blank6}\033[0m coffee. Next, I mix")
    print(f"in \033[1m{blank7}\033[0m. I enjoy drinking this coffee while reading \033[1m{blank8}\033[0m")
    print(f"my java break, I turn into a \033[1m{blank9} {blank10}\033[0m.")

elif choose_madlib == 2:
    blank1_bot = countries[random.randint(0, len(countries))]
    blank2 = input("Enter a type of vehicle (or transportation):  ")
    blank3_bot = places[random.randint(0, len(places))]
    blank4 = input("Enter a type of flavor:  ")
    blank5_bot = plural_nouns[random.randint(0, len(plural_nouns))]
    blank6 = input("Enter a number:  ")
    blank7_bot = verbs[random.randint(0, len(verbs))]
    blank8 = input("Something can hold things inside:  ")
    blank9_bot = adjectives[random.randint(0, len(adjectives))]
    blank10 = input("Enter an adjective:  ")

    print("Standby...")
    time.sleep(5)

    print(f"My family and I love to vacation in {blank1_bot}")
    print(f"We take the {blank2.rstrip} to the {blank3_bot},")
    print(f"and eat {blank4.rstrip()}-covered {blank5_bot} by the")
    print("shore! Sometimes, we stay 10 to 11 days. Other times,")
    print(f"we stay on vacation for {blank6.rstrip()} days!")
    print(f"I like to take photos with my family so I can {blank7_bot}")
    print(f"back on the memories! I even made a {blank8.rstrip()} to")
    print(f"all my {blank9_bot} photos in! I love {blank10.rstrip()} family vacations!")

elif choose_madlib == 2:
    blank1 = input("")
    blank2 = input("")
    blank3 = input("")
    blank4 = input("")
    blank5 = input("")
    blank6 = input("")
    blank7 = input("")
    blank8 = input("")
    blank9 = input("")
    blank10 = input("")

    print("Standby...")
    time.sleep(5)