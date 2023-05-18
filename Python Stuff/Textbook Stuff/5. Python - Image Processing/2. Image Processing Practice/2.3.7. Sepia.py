import image


the_rock = image.Image("the_rock.png")

width = the_rock.getWidth()
height = the_rock.getHeight()

canvas = image.ImageWin(width, height)

the_rock.draw(canvas)


for x in range(width):
    for y in range(height):
        this_pixel = the_rock.getPixel(x, y)

        r = this_pixel.getRed()
        g = this_pixel.getGreen()
        b = this_pixel.getBlue()

        new_r = (r * .393) + (g *.769) + (b * .189)
        new_b = (r * .349) + (g *.686) + (b * .168)
        new_g = (r * .272) + (g *.534) + (b * .131)

        sepia_pixel = image.set_pixel()
