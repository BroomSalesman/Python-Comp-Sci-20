# Have to make two text files, one with entire translated string with non translated string above it, with time it was done. Maybe at the end add number of words translated
# Other is a list of translated words
# Have to figure out how to add everytime to it
import time

VOWELS = "AaEeIiOoUuYy"
PUNCTUATIONS = ".,!?"


def piece_string(string: str):
    pieced_string = string.split(" ")

    # To create sublists for strings with punctuation at end or hyphen in between to ensure proper pig latin conversion
    for word in pieced_string:
        index = pieced_string.index(word)

        # Adds a ♠ in between the punctuation and letter before punctuation so ♠ can be used as a separating marker
        if word[-1] in PUNCTUATIONS:
            pieced_string[index] = word.replace(word[-1], f"♠{word[-1]}")
            # Example: Hello! is turned into Hello♠! , because word[-1]  ("!") was replaced by ♠ + word[-1]. which was "!" from  our example, "Hello!" .
            # Concise example: "Hello" + "!" --> "Hello" + "♠!"

    # Adds a ♠ before and after a hyphen to be used as a seperating marker
    for word in pieced_string:
        index = pieced_string.index(word)
        if "-" in word:
            pieced_string[index] = word.replace("-", "♠-♠")

    # Seperates every string in the list pieced_string into sublists with strings inside, using ♠ as marker for splitting in it strings into lists.
    # Example: "Spider♠-♠Man♠!" -->  ["Spider", "-", "Man", "!"]
    for word in pieced_string:
        index = pieced_string.index(word)
        if "♠" in word:
            pieced_string[index] = word.split("♠")


    return pieced_string


def pig_latinize(string: str):
    capital_check = string[0] == string[0].upper()

    for char in string:
        if char in VOWELS:
            prefix = string[string.index(char):]
            middle = string[:string.index(char)]

            suffix = "yay" if string[0] in VOWELS else "ay"

            break

    pig_latin_word = (prefix + middle + suffix).lower()

    if capital_check is True:
        return pig_latin_word.title()
    else:
        return pig_latin_word




def translate_and_join_sublist(sublist_strings: list):
    index = 0
    for item in sublist_strings:
        if not item in PUNCTUATIONS + "-":
            sublist_strings[index] = pig_latinize(item)


        index += 1

    return "".join(sublist_strings)




def process_strings(string: str):
    string_list = piece_string(string)

    translated_strings = []

    index = 0
    for item in string_list:

        if isinstance(item, list):
            translated_strings.append(translate_and_join_sublist(item))

        elif item.isnumeric():
            translated_strings.append(index)

        else:
            translated_strings.append(pig_latinize(item))

    return " ".join(translated_strings)



"""
def remove_empty_strings (list_of_strings: list):
    # sourcery skip: convert-to-enumerate
    index = 0
    for item in list_of_strings:
        if list_of_strings[index] == {" ", "\n", ""}:
            del list_of_strings[index]
        index += 1
    return list_of_strings
"""

#----------------------------------------------------------------------------------------------------------------------
def format_lines(the_string: str, line_length: int):
    words_per_line = 0

    words_in_string = the_string.split(" ")
    formatted_lines = []

    for _ in range((len(words_in_string)//line_length) + 1):

        formatted_lines.append(" ".join(words_in_string[:line_length]))
        del words_in_string[:line_length]

    return "\n".join(formatted_lines)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


def record_results(original_string: str, pig_latin_string: str):
    translation_record = open("translation-record.txt", "a")
    formatted_original_string = (format_lines(original_string, 20))
    formatted_pig_latin = (format_lines(original_string, 20))
    translation_record.write(f"{time.ctime()}:\n")
    translation_record.write("Original:\n")
    translation_record.write(formatted_original_string + "\n\n")
    translation_record.write("Pig Latin:\n")
    translation_record.write(formatted_pig_latin + "\n\n")



user_string = str(input("Type in your text, and press enter when you are done:\n      "))
pig_latinized_string = process_strings(the_string)

print("\n\n\n\n\n")
print(process_strings(the_string))
print("\n\n\n")

record_results(the_string, pig_latinized_string)
