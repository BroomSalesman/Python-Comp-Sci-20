# Labeeb Farooqi
# HPO267
# 11432366
from time import sleep
import random


def get_name():
    print("You will be prompted to enter your first, middle, and last name one by one in the console.")

    print("Before you do, please read how to enter it correctly.")
    sleep(3)

    print("If part of your name has internal capitalization (i.e, McDaniels), enter a caret (^) between the lowercase and uppercase letter.\n")
    sleep(1.5)

    print("Example: McDaniels would be typed in as Mc^Daniels")
    sleep(2)

    print("\nIf parts of your name are intentionally not capitalized (i.e, van Beethoven), type an asterisk (*) before the non-capitalized part of the name")
    sleep(1.5)

    print("Example: Uz zama would be typed in as Uz *zama, van Beethoven would be *van Beethoven"
    sleep(2.5)

    print("\nYou can do this with your name even if it has a hyphen before the lower case part. \nJean-de-Dieu would be written as Jean-^de-Dieu")

    print("\nYou will now be prompted to enter each part of your name. If you don't have a middle press enter without typing anything.")
    sleep(3)


    first_list = "Jean-*de-*le-DieuMac^Beth^seth".split()#(input("Enter first name (remember to use ^ or * if needed) ")).split()
    middle_list = "Mc^Daniels".split()#(input("Enter middle name (press enter if you dont have one, refer to ^ and * usage if needed)")).split()
    last_list = "*da Vinci* *dyke *jean^be^th".split() #(input("Enter last name (refer to ^ and * usage if needed)")).split()

    raw_names = [first_list, middle_list, last_list]
    edited_names = [[], [], []]

    #Uses nested loops to go through the each item in the three lists, and capitalizes each part of the names while preserving medial capitals and intentional lowercases
    for name in range(len(raw_names)):
        for part in range(len(raw_names[name])):
            edited_part = (raw_names[name][part].title()).replace("^", "")

            edited_part = edited_part.rstrip("*") # Removes trailing "*" to prevent index errors later

            edited_names[name].append(edited_part) #adds each name as an item in a sublist categorized by first, middle and last name

            for i in range(edited_names[name][part].count("*")):
                asterisk_index = edited_names[name][part].index("*")

                if asterisk_index == len(edited_names[name][part]) - 1:
                    edited_names[name][part] = edited_names[name][part].rstrip('*')

                #Uses slicing to replace a *A with a lowercase a, for any letter, eliminating the "*"
                edited_names[name][part] = edited_names[name][part][:asterisk_index] + edited_names[name][part][asterisk_index+1: asterisk_index+2].lower() + edited_names[name][part][asterisk_index+2:]

def get_initials():
    x, y, z = def
    return(x[0]+y[0]+z[0])

def get_username_number():
    return(random.randint(100, 999))



    return " ".join(edited_names[0]), " ".join(edited_names[1]), " ".join(edited_names[2])



# Gets name and splits it into first, middle, and last, and uses hyphens if any part of the name


x, y, z = get_name()


