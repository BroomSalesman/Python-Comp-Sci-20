# Take apart a string using a for loop, and split the word for every space.
# If there is a punctuation, create a sublist.
# First check for sublists, join them
#Then loop back and join all of them
# When I rejoin the translated string, I will first join the translated sub strings with no spaces

def piece_string(string):
    return string.split(" ")

def separate_punctuation(list_of_strings):
    for word in list_of_strings:
        if word[-1] in ".,!?":
            list_of_strings[list_of_strings.index(word)] = word[:-1] + "♠" + word[-1:]
    
    for item in list_of_strings:
        if type(item) == 'list':
            return True


the_string = "The green! monkey ran over the tree or something like that"


print(separate_punctuation(piece_string(the_string)))