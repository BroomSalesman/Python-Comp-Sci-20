
#COME BACK TO UNDERSTAND ALL OF THIS LATER

import pygame as pg
import math
from settings import *


class RayCasting:
    def __init__(self, game):
        self.game = game
        self.ray_casting_result = []
        self.objects_to_render = []
        self.textures = self.game.object_renderer.wall_textures


    def get_objects_to_render(self):
        """Gets the parameters calculated as a result of raycasting and based on them for each ray
        select a subsurface in the form of a rectangle from the initial texture

        """
        self.objects_to_render = []
        for ray, values in enumerate (self.ray_casting_result):
            depth, projection_height, texture, offset = values

            if projection_height < HEIGHT:
                wall_column = self.textures[texture].subsurface(offset * (TEXTURE_SIZE - SCALE), 0, SCALE, TEXTURE_SIZE)

                wall_column = pg.transform.scale(wall_column, (SCALE, projection_height))
                wall_position = (ray * SCALE, HALF_HEIGHT - projection_height // 2)

            else:
                texture_height = TEXTURE_SIZE * HEIGHT / projection_height
                wall_column = self.textures[texture].subsurface(
                    offset * (TEXTURE_SIZE - SCALE),
                    HALF_TEXTURE_SIZE - texture_height // 2, SCALE, texture_height)
                wall_column = pg.transform.scale(wall_column, (SCALE, HEIGHT))

                # It's pretty cool how simple this is due to raycasting code.
                wall_position = (ray * SCALE, 0)

            self.objects_to_render.append((depth, wall_column, wall_position))


    # To super-summarize this, this all just a bunch of code to figure out where a straight line hits and at what points, and the distance from the source of the straight line to the point of collision of the straight line. Like a ray of light (which is why it's called ray-casting)

    # Trigonometry used along with grid map to make this much much easier. Pictures provided for logic
    def ray_cast(self):
        self.ray_casting_result = []
        ox, oy = self.game.player.position  # Coordinate of player on map
        x_map, y_map = self.game.player.map_position  # Coordinate of the tile player is on

        texture_horizontal = 1

        texture_vertical = 1

        ray_angle = self.game.player.angle - HALF_FOV + 0.0001

        for ray in range(NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            #horizontals

            y_horizontal, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)

            depth_horizontal = (y_horizontal - oy) / sin_a
            x_horizontal = ox + depth_horizontal * cos_a

            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for i in range(MAX_DEPTH):
                tile_horizontal = int(x_horizontal), int(y_horizontal)
                if tile_horizontal in self.game.map.world_map:
                    texture_horizontal = self.game.map.world_map[tile_horizontal]
                    break
                x_horizontal += dx
                y_horizontal += dy
                depth_horizontal += delta_depth


            # verticals
            x_vertical, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)

            depth_vertical = (x_vertical - ox) / cos_a     # cos_a = (x_vert - ox) / depth_vert
            y_vertical = oy + depth_vertical * sin_a    # sin_a = (y_vert - oy) / depth_vert

            delta_depth = dx / cos_a    # cos_a = dx / delta_depth
            dy = delta_depth * sin_a    # sin_a = dy / delta_depth

            for i in range(MAX_DEPTH):
                tile_vertical = int(x_vertical), int(y_vertical)
                if tile_vertical in self.game.map.world_map:
                    texture_vert = self.game.map.world_map[tile_vertical]
                    break

                x_vertical += dx
                y_vertical += dy
                depth_vertical += delta_depth



            # depth
            if depth_vertical < depth_horizontal:
                depth, texture = depth_vertical, texture_vertical
                y_vertical %= 1
                offset = y_vertical if cos_a > 0 else (1 - y_vertical)
            else:
                depth, texture = depth_horizontal, texture_horizontal
                x_horizontal %= 1
                offset = (1 - x_horizontal) if sin_a > 0 else x_horizontal


            # draw for debug  LEARN WHAT THE MATH HERE IS FOR LATER
            pg.draw.line(self.game.screen, 'hotpink', (100 * ox, 100 * oy), (100 * ox + 100 * depth * cos_a, 100 * oy + 100 *depth * sin_a), 2)


            #Remove fishbowl effect
            depth *= math.cos(self.game.player.angle - ray_angle)
            #projection
            projection_height = SCREEN_DISTANCE / (depth + 0.0001)
            # ray casting result
            self.ray_casting_result.append((depth, projection_height, texture, offset))

            ray_angle += DELTA_ANGLE



    def  update(self):
        self.ray_cast()
        self.get_objects_to_render()
