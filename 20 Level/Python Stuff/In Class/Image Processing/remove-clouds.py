import image

img = image.Image("bird-far.jpg")
width = img.get_width()
height = img.get_height()

window = image.ImageWin(width, height)
img.draw(window)

for x in range(width):
    for y in range(height):
        this_pixel = img.get_pixel(x, y)

        r = this_pixel.get_red()
        g = this_pixel.get_green()
        b = this_pixel.get_blue()

        if r >= 200 and g <= 200 and b <= 200:
            new_red = 255
            new_green = 255
            new_blue = 255
        else:
            new_red = r
            new_green = g
            new_blue = b


        new_pixel = image.Pixel(new_red, new_green, new_blue)
        img.set_pixel(x, y, new_pixel)
    img.draw(window)
