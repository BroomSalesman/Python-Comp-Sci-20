import image

img = image.Image("skflag.png")
width = img.get_width()
height = img.get_height()

canvas =  image.ImageWin(width, height)
img.draw(canvas)

# Look at every pixel
for x in range(width):
    for y in range(height):
        the_pixel = img.get_pixel(x, y)

        r = the_pixel.get_red()
        g = the_pixel.get_green()
        b = the_pixel.get_blue()

        new_pixel = image.Pixel(r - 50, g - 50, b - 50)

        img.set_pixel(x, y, new_pixel)

    img.draw(canvas)