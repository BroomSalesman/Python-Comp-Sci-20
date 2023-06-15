from ursina import *


class Game(Ursina):
    def __init__(self):
        super().__init__()
        window.fullscreen = True
        Entity(model = 'quad', scale = 60, texture = 'white_cube', texture_scale = (60, 60), rotation_x = 90, y = -5,
               color = color.light_gray) # The plane
        Entity(model = 'sphere', scale = 100, texture = 'textures/pool-tile-texture.png', double_sided = True) # the sky
        Entity(model = 'models/xyz', texture = 'textures/xyz', scale = 0.8) # left-handed xyz plane
        EditorCamera()
        camera.world_position (0, 0, -15)

        self.load_game()

    def load_game(self):
        pass

    def input(self, key):
        super().input(key)


def create_cube_positions():



game = Ursina()

the_plane = Entity(model = "quad", scale = 60, texture = "white_cube", texture_scale = (60, 60), rotation_x = 90, y = -5, color = color.light_gray)

sky = Entity(model = "sphere", scale = 100, texture = "textures/pool-tile-texture.png", double_sided = True) # The sky

xyz_arrows = Entity(model = "models/xyz", texture = "textures/xyz", scale = 0.8)

EditorCamera()
camera.world_position(0, 0, -15)

app.run()

