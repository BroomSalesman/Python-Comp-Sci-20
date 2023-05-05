import random

with open("adjective.txt", "r", encoding="utf-8") as file:
    adjectives = file.readlines()
adjectives = [line.strip() for line in adjectives]
with open("adverbs.txt", "r", encoding="utf-8") as file:
    adverbs = file.readlines()
adverbs = [line.strip() for line in adverbs]
with open('nouns.txt', 'r', encoding='utf-8') as file:
    nouns = file.readlines()
nouns = [line.strip() for line in nouns]
with open('verbs.txt', 'r', encoding='utf-8') as file:
    verbs = file.readlines()
verbs = [line.strip() for line in verbs]
with open('verb-ing.txt', 'r', encoding='utf-8') as file:
    verb_ings = file.readlines()
verb_ings = [line.strip() for line in verb_ings]
with open('countries.txt', 'r', encoding='utf-8') as file:
    countries = file.readlines()
countries = [line.strip() for line in countries]
with open('places.txt', 'r', encoding='utf-8') as file:
    places = file.readlines()
places = [line.strip() for line in places]
with open('plural-nouns.txt', 'r', encoding='utf-8') as file:
    plural_nouns = file.readlines()
plural_nouns = [line.strip() for line in plural_nouns]
with open('names.txt', 'r', encoding="utf-8") as file:
    names = file.readlines()
names = [line.strip() for line in names]
with open("clothings-accessories.txt", "r", encoding="utf-8") as file:
    clothings_accessories = file.readlines()
clothings_accessories = [line.strip for line in clothings_accessories]
with open("fluids.txt", "r", encoding="utf-8") as file:
    fluids = file.readlines()
fluids = [line.strip() for line in fluids]
print("\n\n\n\n\n\n\n  In case you don't know what a madlib is, press N and ENTER.\n If you do know what a mad lib is, only press ENTER")
continue1 = input("")
if continue1 == "N":
    print("\n\nA madib is a game/interactive-story that takes words from the player/reader to fill in little gaps in the story.")
    print("The blanks usually have a little word below them, to determine what the word should be. The basic specifications are nouns, adjectives, verbs, adverbs, names, etc.,")
    print("but there are also more specific blanks, such as 'a type of food', 'something that flies', 'a country', etc.")
    print("You will not get to see the madlib before choosing words first for this madlib.")
    continue2 = input("Press enter once you have finished reading.")
print("\nYou have 3 different types of madlibs to choose from:\n")
print("1. A madlib in which you choose all the words.")
print("2. A madlib in which you choose half of the words and the rest are randomly generated.")
print("3. A madlib in which all the words are computer generated.\n")
possible_selections = [1, 2, 3]
while True:
    try:
        choose_madlib = int(
            input("To select one, press 1, 2, or 3, then press enter (see above):\n"))
        if choose_madlib not in possible_selections:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Try again.")
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
    
    print(f"\n\n\n\n\n\n\n\nDo not \033[1m{blank1.rstrip()}\033[0m to me before I have had my coffee! Before I get my first sip, I am \033[1m{blank2.rstrip()}\033[0m. If I do not get")
    print(f"to practice my morning routine, then the day is sure to be \033[1m{blank3.rstrip()}\033[0m. First I get \033[1m{blank4.rstrip} {blank5.rstrip()}\033[0m mug.")
    print(f"Then I brew some \033[1m{blank6.rstrip()}\033[0m coffee. Next, I mix in \033[1m{blank7.rstrip()}\033[0m. I enjoy drinking this coffee while reading \033[1m{blank8.rstrip()}\033[0m")
    print(f"my java break, I turn into a \033[1m{blank9.rstrip()} {blank10.rstrip()}\033[0m.")

elif choose_madlib == 2:
    blank1_bot = countries[random.randint(0, len(countries)-1)]
    blank2 = input("Enter a type of vehicle (or transportation):  ")
    blank3_bot = places[random.randint(0, len(places)-1)]
    blank4 = input("Enter a type of flavor:  ")
    blank5_bot = plural_nouns[random.randint(0, len(plural_nouns)-1)]
    blank6 = input("Enter a number:  ")
    blank7_bot = verbs[random.randint(0, len(verbs)-1)]
    blank8 = input("Something can hold things inside:  ")
    blank9_bot = adjectives[random.randint(0, len(adjectives)-1)]
    blank10 = input("Enter an adjective:  ")
   
    print("Standby...")
   
    print(f"My family and I love to vacation in \033[1m{blank1_bot.rstrip()}\033[0m. We take the \033[1m{blank2.rstrip()}\033[0m to the \033[1m{blank3_bot.rstrip()}\033[0m,")
    print(f"and eat \033[1m{blank4.rstrip()}\033[0m-covered \033[1m{blank5_bot.rstrip()}\033[0m by the shore! Sometimes, we stay 10 to 11 days. Other times,")
    print(f"we stay on vacation for \033[1m{blank6.rstrip()}\033[0m days! I like to take photos with my family so I can \033[1m{blank7_bot}\033[0m")
    print(f"back on the memories! I even made a \033[1m{blank8.rstrip()}\033[0m to all my \033[1m{blank9_bot.rstrip()}\033[0m photos in! I love \033[1m{blank10.rstrip()}\033[0m family vacations!")

elif choose_madlib == 3:
    blank1 = random.randint(0, 10)
    blank2 = names[random.randint(0, len(names)-1)]
    blank3 = verb_ings[random.randint(0, len(verb_ings)-1)]
    blank4 = clothings_accessories[random.randint(
        0, len(clothings_accessories)-1)]
    blank5 = verb_ings[random.randint(0, len(verb_ings)-1)]
    blank6 = adjectives[random.randint(0, len(adjectives)-1)]
    blank7 = verb_ings[random.randint(0, len(verb_ings)-1)]
    blank8 = adjectives[random.randint(0, len(adjectives)-1)]
    blank9 = nouns[random.randint(0, len(nouns)-1)]
    blank10 = fluids[random.randint(0, len(fluids)-1)]

    print("Standby...")
    print(f"Magicians have been around for \033[1m{blank1.rstrip}\033[0m centuries. One famous magician was named \033[1m{blank2.rstrip()}\033[0m the \033[1m{blank3.rstrip()}\033[0m trickster!")
    print(f"He had 21 invisibility \033[1m{blank4.rstrip()}\033[0m, twelve {blank5.rstrip()} doves, and one {blank6.rstrip()} talking lion. He roamed the earth searching")
    print(f"for an apprentice. However, all he found was a(n) {blank7.rstrip()}, annoying, {blank8.rstrip()}, smelly, troll. This was no ordinary troll, though! It was")
    print(f"a magical one, who quickly turned the magician into a {blank9.rstrip()}, and tossed him into {blank10.rstrip().title()} Volcano. Yikes!")
