from settings import *
import pygame as pg
import math

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def movement(self):
        # I understand why this is here.
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a


        # I see how there's negative values just like how Mr. Schellenberg showed us in Scratch at the start of the semester
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin

        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin

        if keys[pg.K_a]:
            dx  += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos

        # Wall collision rules used here since wall collision rules are technically
        # just movement rules, with increasing/decreasing dx and dy values.
        self.check_for_wall_collision(dx, dy)

        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROTATION_SPEED * self.game.delta_time

        if keys[pg.K_RIGHT]:
            # The path of the player
            self.angle += PLAYER_ROTATION_SPEED * self.game.delta_time
        self.angle %= math.tau

    def check_for_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_for_wall_collision(self, dx, dy):
        if self.check_for_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_for_wall(int(self.x), int(self.y + dy)):
            self.y += dy

    def draw(self):
        pg.draw.line(self.game.screen, 'pink', (self.x * 100, self.y * 100), (self.x * 100 + WIDTH * math.cos(self.angle), self.y *100 + WIDTH * math.sin(self.angle)), 2)

        pg.draw.circle(self.game.screen, 'yellow', (self.x * 100, self.y * 100), 15)

    def update(self):
        self.movement()

    # A built in decorator for the property() function in Python.
    # Used to give a special functionality to certain method to make them act
    # as getters, setters, or deleters we define properties in a class.
    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)


