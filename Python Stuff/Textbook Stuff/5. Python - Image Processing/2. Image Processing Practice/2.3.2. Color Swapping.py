import image
import time

img = image.Image("the_rock2.png")

width = img.get_width()
height = img.get_height()

canvas  = image.ImageWin(width, height)
img.draw(canvas)

for x in range(width):
    for y in range(height):
        pixel = img.get_pixel(x, y)

        r = pixel.get_red()
        g = pixel.get_green()
        b = pixel.get_blue()



