import pygame as pg
from settings import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()


    # learn what this is later
    @staticmethod
    def get_texture(path, res = (TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha() #learn what this does
        return pg.transform.scale(texture, res)

    def load_wall_textures(self):
        return {
            1: self.get_texture('textures/1.png'),
            2: self.get_texture('textures/2.png'),
            3: self.get_texture('textures/3.png'),
            4: self.get_texture('textures/4.png'),
            5: self.get_texture('textures/5.png')
        }
