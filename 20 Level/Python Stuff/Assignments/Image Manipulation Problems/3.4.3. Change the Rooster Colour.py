import image
import time

rooster = image.Image("rooster.jpg")

width = rooster.getWidth()
height = rooster.getHeight()

canvas = image.ImageWin(width, height)

rooster.draw(canvas)
print(width)
print(height)
for x in range(width):
    for y in range(height):
        the_pixel = rooster.get_pixel(x , y)

        r = the_pixel.getRed()
        g = the_pixel.getGreen()
        b = the_pixel.getBlue()


        if r - g > 50 or r -b > 80 or 50 < (r + g + b) - r / 3 < 30: # last part was part of some experimenting
        #if r > 210:
            new_r = 0
            new_g = g
            new_b = r

        else:
            new_r = r
            new_g = g
            new_b = b

        new_pixel = image.Pixel(new_r, new_g, new_b)

        if  200 <= x <= 290 and  60 <= y <= 200:
            rooster.set_pixel(x, y, new_pixel)

    rooster.draw(canvas)

time.sleep(5)
