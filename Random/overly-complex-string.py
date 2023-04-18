# Define a function to generate a random integer
from random import randint

def generate_random_int():
    return randint(1, 3)

# Define a function to generate a random letter
import string

def generate_random_letter():
    alphabet = string.ascii_letters + "0123456789"
    letter_index = randint(0, len(alphabet) - 1)
    return alphabet[letter_index]

# Define a function to generate a random word
def generate_random_word(length):
    word = ""
    for i in range(length):
        word += generate_random_letter()
    return word

# Define variables to store the word "Monkey"
m = generate_random_word(generate_random_int())
o = generate_random_word(generate_random_int())
n = generate_random_word(generate_random_int())
k = generate_random_word(generate_random_int())
e = generate_random_word(generate_random_int())
y = generate_random_word(generate_random_int())

# Concatenate the variables to print the word "Monkey"
print(m + "-" + o + "-" + n + "-" + k + "-" + e + "-" + y)