import image


shoes = image.Image("sneakers.jpg")

width = shoes.getWidth()
height = shoes.getHeight()

canvas = image.ImageWin(width, height)

shoes.draw(canvas)


for x in range(width):
    for y in range(height):
        this_pixel = shoes.getPixel(x, y)

        r = this_pixel.getRed()
        g = this_pixel.getGreen()
        b = this_pixel.getBlue()

        # From stackoverflow link (on the practice problem)
        new_r = (r * .393)//1 + (g *.769)//1 + (b * .189)//1 # Thought integer dividing might solve a problem I was having.
        new_g = (r * .349)//1 + (g *.686)//1 + (b * .168)//1 # Turned out the problem was just me using new_b when I should have used new_g (in the sepia_pixel variable)
        new_b = (r * .272)//1 + (g *.534)//1 + (b * .131)//1 # Kept this here anyways since why not? I'm showing I know what integer dividing does.

        if new_r > 255:
            new_r = 255

        if new_g > 255:
            new_g = 255

        if new_b > 255:
            new_b = 255

        sepia_pixel = image.Pixel(new_r, new_g, new_b)
        shoes.set_pixel(x, y, sepia_pixel)

    shoes.draw(canvas)
