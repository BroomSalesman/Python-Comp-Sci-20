import image
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import os

import collections
from _collections_abc import Iterable
collections.Iterable = Iterable            # To fix "collections has no attribute 'Iterable'" error I get if I don't do this.

current_dir = os.path.dirname(os.path.abspath(__file__))
subfolder = "layers"
subfolder_path = os.path.join(current_dir, subfolder)

#pos = mc.player.getTilePos()
#mc = minecraft.Minecraft.create()

y = 0
print(subfolder_path)
for filename in os.listdir(subfolder_path):

    layer = image.Image(filename)

    x_coordinates =  layer.get_width()
    y_coordinate = y
    z_coordinates = layer.get_height()

    canvas = image.ImageWin(x_coordinates, z_coordinates)

    layer.draw(canvas)

    for x in range(x_coordinates):
        for z in range(z_coordinates):
            #time.sleep(0.05)                            This was part of original code, but I hashtagged it out and changed the purpose of this test file
            #mc.setBlock(pos.x + 3 + x, y, pos.z + z)                        Same here
            this_pixel = layer.get_pixel(x, z)

            red = this_pixel.getRed()
            green = this_pixel.getGreen()
            blue = this_pixel.getBlue()

            new_red = red - 40
            new_green = green  - 70
            new_blue = blue - 120

            new_pixel = image.Pixel(new_red, new_green, new_blue)
            layer.set_pixel(x, z, new_pixel)
        layer.draw(canvas)
    y += 1





    y += 1


