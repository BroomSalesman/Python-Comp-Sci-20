import pygame as pg
from settings import *


class SpriteObject:
    def __init__(self, game, path = 'sprites/static_sprites/candles.png', position = (10.5, 3.5)):
        self.game = game
        self.player = game.player
        self.x, self.y = position
        self.image = pg.image.load(path).convert_alpha()
        self.IMAGE_WIDTH = self.image.get_width()
        self.IMAGE_HALF_WIDTH = self.image.get_width() // 2
        self.IMAGE_RATIO = self.IMAGE_WIDTH / self.image.get_height()
        self.dx, self.dy, self.theta, self.screen_x, self.distance, self.normal_distance = 0, 0, 0, 0, 1, 1
        self.sprite_half_width = 0

    def get_sprite_projection(self):
        projection = SCREEN_DISTANCE / self.normal_distance
        projection_width, projection_height = projection * self.IMAGE_RATIO, projection

        image  = pg.transform.scale(self.image, (projection_width, projection_height))

        self.sprite_half_width = projection_width // 2
        position = self.screen_x - self.sprite_half_width, HALF_HEIGHT - projection_height // 2
        self.game.raycasting.objects_to_render.append((self.normal_distance, image, position))

    def get_sprite(self):
        dx = self.x - self.player.x
        dy = self.y - self.player.y
        self.dx, self.dy = dx, dy
        self.theta = math.atan2(dy, dx)

        delta = self.theta - self.player.angle
        if (dx > 0 and self.player.angle > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau

        # ray between casted ray and sprite
        delta_rays = delta / DELTA_ANGLE
        self.screen_x = (HALF_NUM_RAYS + delta_rays) * SCALE

        self.distance = math.hypot(dx, dy)
        self.normal_distance = self.distance * math.cos(delta)
        if -self.IMAGE_HALF_WIDTH < self.screen_x < (WIDTH + self.IMAGE_HALF_WIDTH) and self.normal_distance > 0.5:
            self.get_sprite_projection()

    def update(self):
        self.get_sprite()
