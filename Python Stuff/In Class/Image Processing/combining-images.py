import image

rooster = image.Image("rooster.jpg")
width = rooster.get_width()
height = rooster.get_height()

smile = image.Image("smile.png")
smile_width = smile.get_width()
smile_height = smile.get_height()

canvas = image.ImageWin(width, height)
rooster.draw(canvas)
smile.draw(canvas)


for x in range(int(smile_width)):
    for y in range(smile_height):
        smile_pixel = smile.get_pixel(x, y)

        r_smile = smile_pixel.get_red()
        g_smile = smile_pixel.get_green()
        b_smile = smile_pixel.get_blue()

        if r_smile < 250 and g_smile < 250 and b_smile < 250:
            rooster.set_pixel(x + 150, y + 50, smile_pixel)

    rooster.draw(canvas)
