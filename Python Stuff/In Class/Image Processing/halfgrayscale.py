import image

shoes = image.Image("sneakers.jpg")
width = shoes.get_width()
height = shoes.get_height()

canvas = image.ImageWin(width, height)

shoes.draw(canvas)

for x in range(int(width/2)):
    for y in range(height):
        pixel = shoes.get_pixel(x, y)

        r = pixel.get_red()
        g = pixel.get_green()
        b = pixel.get_blue()

        grayscale = (r + g + b) / 3

        new_pixel = image.Pixel(grayscale, grayscale, grayscale)

        shoes.set_pixel(x, y, new_pixel)

    shoes.draw(canvas)
