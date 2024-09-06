from ursina import *
from random import uniform
from ursina.prefabs.first_person_controller import FirstPersonController

# ignore


def input(key):
    if key == "left mouse down":
        Audio("assets/laser_sound.wav")  # change later
        Animation("assets/spark", parent=camera.ui, fps=5, scale=0.1, position=(0.19, -0.03), loop=False)

        for wasp in wasps:
            if wasp.hovered:
                destroy(wasp)


class Wasp(Button):
    def __init__(self, x, y, z):
        super().__init__(
            parent=scene,
            model="assets/wasps.obj",
            scale=0.1,
            position=(x, y, z),
            rotation=(0, 90, 0),
            collider="box"
        )


class Spider(Button):
    def __init__(self, x, y, z):
        super().__init__(
            parent=scene,
            model="asset/spider.obj",
            scale=0.2,
            position=(x, y, z),
            rotation=(0, 90, 0),
            collider="box"
        )


app = Ursina()

Sky()
player = FirstPersonController(y=2, origin_y=-.5)
ground = Entity(model='plane', scale=(100, 1, 500), color=color.lime, texture="white_cube", texture_scale=(100, 100), collider='box')

wall_1 = Entity(model="cube", collider="box", position=(-8, 0, 0), scale=(8, 5, 1), rotation=(0, 0, 0), texture="brick", texture_scale=(5, 5), color=color.rgb(255, 128, 0))
wall_2 = duplicate(wall_1, z=5)
wall_3 = duplicate(wall_1, z=10)
wall_4 = Entity(model="cube", collider="box", position=(-15, 0, 10), scale=(1, 5, 20), rotation=(0, 0, 0), texture="brick", texture_scale=(5, 5), color=color.rgb(255, 128, 0))

gun = Entity(model="assets/gun.obj", parent=camera.ui, scale=0.08, color=color.gold, position=(0.3, -0.2), rotation=(-5, -10, -10))

numero = 10
wasps = [None] * numero
spiders = [None] * numero

for i in range(numero):
    wx = uniform(-12, -7)
    wy = uniform(0.1, 1.8)
    wz = uniform(0.8, 3.8)
    wasps[i] = Wasp(wx, wy, wz)
    wasps[i].animate_x(wx + 0.5, duration=0.2, loop=True)
for i in range(numero):
    sx = uniform(-12, -7)
    sy = uniform(0.1, 1.8)
    sz = uniform(5.8, 8.8)
    spiders[i] = Spider(sx, sy, sz)
    spiders[i].animate_x(sx + 0.5, duration=0.2, loop=True)

app.run()
