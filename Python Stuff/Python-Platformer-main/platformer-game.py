# pylint: disable= missing-function-docstring, unused-import, unused-variable, wrong-import-order, unused-argument, redefined-outer-name
# pylint: disable = consider-using-sys-exit
import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

pygame.init()

pygame.display.set_caption("Platformer Game")


BG_COLOR = (255, 255, 255)  # here until I implement my own background
WIDTH, HEIGHT = 1000, 800
FPS = 120   # Supposed to be 60, if game doesnt work make sure to check this out
PLAYER_VEL = 5  # Speed of player

window = pygame.display.set_mode((WIDTH, HEIGHT))

def get_background(name):  #name is color of background
    image = pygame.image.load(join("assets", "Background", name))
    



def main(window):
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS) #If game super fast, lower FPS line: 17

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)
