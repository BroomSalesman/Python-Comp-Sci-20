import pygame as pg
from settings import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture("textures/sky.png", (WIDTH, HALF_HEIGHT))
        self.sky_offset = 0


    def draw(self):
        self.draw_background()
        self.render_game_objects()

    def draw_background(self):
        #sky
        self.sky_offset = (self.sky_offset + 4.5 * self.game.player.relativity) % WIDTH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + WIDTH, 0))

        #floor
        pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT))

    def render_game_objects(self):
        """get access to a list of objects for rendering, iterate over the list and draw the resulting texture columns on the rendering screen
        """
        list_objects = sorted(self.game.raycasting.objects_to_render, key = lambda t: t[0], reverse = True)
        for depth, image, position in list_objects:
            self.screen.blit(image, position)


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
