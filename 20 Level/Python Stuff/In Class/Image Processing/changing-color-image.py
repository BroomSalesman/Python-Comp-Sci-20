import image
import random

img = image.Image("the_rock.png")
width = img.get_width()
height = img.get_height()

canvas =  image.ImageWin(width, height)
img.draw(canvas)

r1 = random.randint(0, 255)
g1 = random.randint(0, 255)
b1 = random.randint(0, 255)


# Look at every pixel
for x in range(width):
    for y in range(height):

            the_pixel = img.get_pixel(x, y)

            r = the_pixel.get_red()
            g = the_pixel.get_green()
            b = the_pixel.get_blue()

            new_pixel = image.Pixel(abs(b - b1) , abs(g - g1), abs(r - r1))

            img.set_pixel(x, y, new_pixel)


img.draw(canvas)
img.save("hi")


