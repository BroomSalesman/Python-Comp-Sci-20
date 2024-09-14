"""Bagels, a deductive logic game.
By Labeeb Farooqi and tutorial for this logic game by Al Sweigart
A deductive logic game where you must guess a number based on clues.
This code is available at https://nostarch.com/big-book-small-python-programming
A version of this game is featured in the book, "Invent Your Own Computer
Games with Python" https://nostarch.com/inventwithpython
Tags: short, game, puzzle"""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10

wrong_place = "Pico"
right_place = "Fermi"
incorrect = "Bagels"


def main():
    print(f'''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com

I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
Try to guess what is. Here are some clues:

When I say:          That means:
    {wrong_place}    One digit is correct but in the wrong position.
    {right_place}     One digit is correct and in the right position.
    {incorrect}        No digit is correct.

For example, if the secret number was 248 and your guess 843, the
clues would be Fermi Pico.''')


