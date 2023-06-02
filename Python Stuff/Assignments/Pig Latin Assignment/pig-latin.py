# Take apart a string using a for loop, and split the word for every space.
# If there is a punctuation, create a sublist.
# First check for sublists, join them
#Then loop back and join all of them
# When I rejoin the translated string, I will first join the translated sub strings with no spaces

# If the word starts with a vowel, end = yay
# Else: end = ay
VOWELS = "AaEeIiOoUuYy"
PUNCTUATION = ".,!?"

def piece_string(string):
    return string.split(" ")



def separate_punctuation(string_list):
    for word in string_list:
        if word[-1] in ".,!?":
            string_list[string_list.index(word)] = word[:-1] + "♠" + word[-1:]
        
    for word in string_list:
        if "♠" in word:
            string_list[string_list.index(word)] = word.split("♠")



def translate_string(string):
    
    capital_check = string[0] == string[0].upper()
    
    for char in string:
        if char in VOWELS:
            prefix = string[string.index(char):]
            middle = string[:string.index(char)]
            
            if string[0] in VOWELS:
                suffix = "yay"
            else:
                suffix = "ay"
            break
        
        translated_word = (prefix + middle + suffix).lower()
    
    if capital_check == True:
        return translated_word.title()
    else:
        return translated_word
                    

def translate_sublist_strings(string_list):
    for item in string_list:
        if type(item) == "list":
             for string in item:
                 if string in PUNCTUATION:
                     continue
                 elif True:
                     translate_string()

def process_strings(string_list):
    # Initatialize empty list
    translated_strings = []
    
    for item in string_list:
        
        if item.isnumeric() == True:
            translated_strings.append(string_list.pop(string_list.index(item)))
            continue
        
        elif type(item) == "list":
            string_list[string_list.index(item)] == translate_sublist_strings(item)
            string_list = 
                 

the_string = "The green! monkey ran over the tree or something like that"


print(separate_punctuation(piece_string(the_string)))