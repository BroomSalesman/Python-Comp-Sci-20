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
    _,  _, width, height, = image.get_rect()     # Underscores mean don't care about values, x and y
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = [i * width, j * height]
            tiles.append(pos)

    return tiles, image

def draw(window, background):
    for tile in background:
        window.blit()

    pygame.display.update()

def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background(Yellow.png)


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
