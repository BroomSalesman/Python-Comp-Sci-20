#################################################################
# Labeeb Farooqi
# Computer Science 20
# June 1 2023
#
# Pig Latin Converter Program
# Purpose: To translate user input into Pig Latin
################################################################

from datetime import datetime

VOWELS = "AaEeIiOoUuYy"
PUNCTUATIONS = ".,!?"


def piece_string(user_string: str):
    """Splits a string into words in a list, and splits

    Args:
        user_string (str): string to be split into words and sublists containing word and punctuation after it

    Returns:
        pieced_string (list): a list of words, and may include sublists with words, punctuations, and hyphens in them, if words had a punctuation attached to it, or had a hyphens in the word.
    """
    pieced_string = user_string.split(" ")

    # To create sublists for strings with punctuation at end or hyphen in between to ensure proper pig latin conversion
    for item in range(len(pieced_string)):

        # Adds a ♠ in between the punctuation and letter before punctuation so ♠ can be used as a separating marker
        # Example: Hello! is turned into Hello♠! , because word[-1]  ("!") was replaced by ♠ + word[-1]. which was "!" from  our example, "Hello!" .
        # Concise example: "Hello" + "!" --> "Hello" + "♠!"
        for sub_item in range(len(pieced_string[item])):
            if pieced_string[item][sub_item] in PUNCTUATIONS:
                pieced_string[item] = pieced_string[item].replace(pieced_string[item][sub_item], f"♠{pieced_string[item][sub_item]}", 1)
                break

    # Adds a ♠ before and after a hyphen to be used as a seperating marker
    for indice in range(len(pieced_string)):
        if "-" in pieced_string[indice]:
            pieced_string[indice] = pieced_string[indice].replace("-", "♠-♠")


    # Seperates every string in the list pieced_string into sublists with strings inside, using ♠ as marker for splitting in it strings into lists.
    # Example: "Spider♠-♠Man♠!" -->  ["Spider", "-", "Man", "!"]
    for indice in range(len(pieced_string)):
        if "♠" in pieced_string[indice]:
            pieced_string[indice] = pieced_string[indice].split("♠")


    return pieced_string


def pig_latin_rules(string: str):
    """Turns a string (one word) into pig latin, but treats one whole string as one word. "Hi Mr. Schellenberg" will return "Ihay Mray. Ellenbergschay".
    To translate whole sentence, the pig_latin_process_strings() must be used.

    Args:
        string (str): the string to be converted into pig-latin

    Returns:
        pig_latin_word (str): a string
    """

    capital_check = string[0] == string[0].upper()

    # The for loop finds the first instance of a vowel.
    # If it reaches the end of the loop and no vowels are found, then it make the entire string the prefix
    for char in string:
        if char in VOWELS:
            prefix = string[string.index(char):]
            middle = string[:string.index(char)]

            suffix = "yay" if string[0] in VOWELS else "ay"

            break

        else:
            prefix = string
            middle = ""
            suffix = "yay" if string[0] in VOWELS else "ay"


    pig_latin_word = (prefix + middle + suffix).lower()

    if capital_check is True:
        return pig_latin_word.title()
    else:
        return pig_latin_word




def pig_latinize_and_glue_list(list_strings: list, glue: str):
    """Translates the strings in a list into Pig Latin and joins them together using the argument glue as the joiner.

    Args:
        list_strings (list): sublist with strings inside
        glue (str): the string (usually " ") that will join the list together with whatever value glue is in between each item from the sublist

    Returns:
        "".join(list_strings): the joined string with Pig
    """
    for indice in range(len(list_strings)):
        item = list_strings[indice]

        if len(item) == 0:
            continue

        elif item[-1] not in f"{PUNCTUATIONS}-":
            list_strings[indice] =pig_latin_rules(list_strings[indice])


    return glue.join(list_strings)




def pig_latin_process_strings(string: str):
    """Iterates through each string in a list and determines if the string should be translated to Pig Latin or left as it is, and then appended into a new list, then joined together into one entire string.
        Makes use of other functions too, see doc strings for seperatre functions.

    Args:
        string (str):

    Returns:
        pig_latin_string (str): All the words translated and joined together to form one string

    """
    string_list = piece_string(string)

    translated_list = []

    index = 0
    for item in string_list:

        if isinstance(item, list):
            translated_list.append(pig_latinize_and_glue_list(item, ""))

        elif item.isnumeric():
            translated_list.append(index)

        elif len(item) == 0:
            pass


        else:
            translated_list.append(pig_latin_rules(item))

    pig_latin_string = " ".join(translated_list)

    return "".join(pig_latin_string)





#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def format_lines(the_string: str, line_length: int):
    """Takes a string and formats it by word length, so if the line_length is 10, the formatted string will have 10 words per line

    Args:
        the_string (str): the string to be formatted
        line_length (int): number of words per line

    Returns:
        formatted_lines: returns a string with newlines to
    """
    words_in_string = the_string.split(" ")
    list_of_lines = []

    for _ in range((len(words_in_string)//line_length) + 1):

        list_of_lines.append(" ".join(words_in_string[:line_length]))
        del words_in_string[:line_length]

    formatted_lines = "\n".join(list_of_lines)

    return formatted_lines

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


def record_results(original_string: str, pig_latin_string: str):
    """Records the user input and the Pig Latin translation of the user input into a text file. Includes time and date of translation.

    Args:
        original_string (str): original string that the user inputted
        pig_latin_string (str): Pig Latin translation
    """
    translation_record = open("translation-record.txt", "a")

    formatted_original_string = (format_lines(original_string, 20))
    formatted_pig_latin = (format_lines(pig_latin_string, 20))

    translation_record.write(f"\n{(datetime.now()).strftime('%Y-%m-%d %H:%M:%S')}\n")
    translation_record.write("Original:\n")
    translation_record.write(formatted_original_string + "\n\n")
    translation_record.write("Pig Latin:\n")
    translation_record.write(formatted_pig_latin + "\n\n")
    translation_record.write("-" * 100)

print("\n\n")
user_string = str(input("Type in your text, and press enter when you are done (you can also use dashes/hyphens between words):\n"))
pig_latinized_string = pig_latin_process_strings(user_string)

print("\n\n\n\n\n")
print(pig_latin_process_strings(user_string))
print("\n\n\n")

record_results(user_string, pig_latinized_string)
