import image

width = 400
height = 300

canvas = image.ImageWin(width, height)
img = image.EmptyImage(width, height)


the_pixel = image.Pixel(0, 255, 0)
for y in range(height):
    for x in range(width):
        img.set_pixel(x, y, the_pixel)

    img.draw(canvas)
# "Flip book"
