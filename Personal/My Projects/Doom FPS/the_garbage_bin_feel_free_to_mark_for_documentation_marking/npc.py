from sprite_object import *
from random import randint, random, choice


class NPC(AnimatedSprite):
    def __init__(self, game, path = 'sprites/npc/soldier/0.png', pos = (10.5, 5.5),
                scale = 0.6, shift = 0.38, animation_time = 180):
        super().__init__(game, path, pos, scale, shift, animation_time)
        self.attack_images = self.get_images(self.path + '/attack')
        self.death_images = self.get_images(self.path + '/death')
        self.idle_images = self.get_images(self.path + '/idle')
        self.pain_images = self.get_images(self.path + '/pain')
        self.walk_images = self.get_images(self.path + '/walk')

        self.attack_dist = randint(3, 6)
        self.speed = 0.03
        self.size = 10
        self.health = 100
        self.attack_damage = 10
        self.accuracy = 0.15
        self.alive = True
        self.pain = False

def update(self):
    self.check_animation_time()
    self.get_sprite()
    self.run_logic()

def run_logic(self):
    if self.alive:
        self.animate(self.idle_images)


















