# Labeeb Farooqi
# HPO267
# 11432366
from time import sleep


def get_name():
    print("You will be prompted to enter your first, middle, and last name one by one in the console.")
    print("Before you do, please read how to enter it correctly.")
    #sleep(3)
    print("If part of your name has internal capitalization (i.e, McDaniels), enter a caret (^) between the lowercase and uppercase letter.\n")
    #sleep(1.5)
    print("Example: McDaniels would be typed in as Mc^Daniels")
    #sleep(2)
    print("\nIf parts of your name are intentionally not capitalized (i.e, van Beethoven), type an asterisk (*) before the non-capitalized part of the name")
    #sleep(1.5)
    print("Example: Uz zama would be typed in as Uz *zama, van Beethoven would be *van Beethoven")
    #sleep(2.5)
    print("\nYou can do this with your name even if it has a hyphen before the lower case part. \nJean-de-Dieu would be written as Jean-^de-Dieu")

    print("\nYou will now be prompted to enter each part of your name. If you don't have a middle press enter without typing anything.")
    #sleep(3)


    first_list = "Jean-*de-*-le-*Dieu Mac^Beth^seth".split()#(input("Enter first name (remember to use ^ or * if needed) ")).split()
    middle_list = "Mc^Daniels".split()#(input("Enter middle name (press enter if you dont have one, refer to ^ and * usage if needed)")).split()
    last_list = "*da Vinci".split() #(input("Enter last name (refer to ^ and * usage if needed)")).split()

    raw_names = [first_list, middle_list, last_list]
    edited_names = [[], [], []]
    for name in range(len(raw_names)):
        for part in range(len(raw_names[name])):
            edited_part = (part.title()).replace("^", "")
            edited_names[name].append(edited_part)
        for part in edited_names[name]:
            for i in range(part.count("*")):
                asterisk_index = part.index("*")
                #if asterisk_index == len(part)
                edited_names[name][asterisk_index:asterisk_index + 2] = edited_names[name][asterisk_index:asterisk_index + 2]


#replace.()
                #capitalize list first then replace *_ with (index("*"))


    return first_list, middle_list, last_list

    #make sure to do if len(list) > 1 else break
    #Use like a for i in range count(^)
    #replace  ^ with empty space  " " if there are any


# Gets name and splits it into first, middle, and last, and uses hyphens if any part of the name


x, y, z = get_name()

input("test")
