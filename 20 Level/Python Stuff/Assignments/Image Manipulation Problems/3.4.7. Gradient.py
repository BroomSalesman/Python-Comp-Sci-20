import image

width = 255
height = 255

win = image.ImageWin(width, height)
img = image.EmptyImage(width, height)

for x in range(width):
    for y in range(height):

        r = 255 - x
        g = 0 + x
        b = 0

        the_pixel = image.Pixel(r, g, b)
        img.set_pixel(x, y, the_pixel)

img.draw(win)
