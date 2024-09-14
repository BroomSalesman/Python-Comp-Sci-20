import microbit as mcb
import time

word = list("monke")

while "banana" == "banana":
    for letter in word:
        mcb.display.show(letter)
        time.sleep(0.25)
