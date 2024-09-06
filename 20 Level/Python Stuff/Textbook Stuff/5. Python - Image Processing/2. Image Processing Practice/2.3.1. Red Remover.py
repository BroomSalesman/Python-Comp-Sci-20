import image

img = image.Image("the_rock.png")
width = img.get_width()
height = img.get_height()

win = image.ImageWin(width, height)
img.draw(win)

for x in range(width):
    for y in range(height):
        the_pixel = img.get_pixel(x, y)

        r = the_pixel.get_red()
        g = the_pixel.get_green()
        b = the_pixel.get_blue()

        new_pixel = image.Pixel(r - r, g, b)
        img.set_pixel(x, y, new_pixel)

    img.draw(win)
