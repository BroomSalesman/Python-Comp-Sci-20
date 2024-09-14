import image

img = image.Image("rooster.jpg")
width = img.getWidth()
height = img.getHeight()

canvas = image.ImageWin(width, height)
img.draw(canvas)

for x in range(width):
    for y in range(height):
        the_pixel = img.get_pixel(x, y)

        r = the_pixel.get_red()
        g= the_pixel.get_green()
        b = the_pixel.get_blue()

        gray_scale = (r + g + b) / 3
        #image processing / mess with the RGB values . . .

        new_pixel =image.Pixel(gray_scale, gray_scale, gray_scale)
        img.set_pixel(x, y, new_pixel)

    img.draw(canvas)
