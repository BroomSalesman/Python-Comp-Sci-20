import image

the_rock = image.Image("the_rock.png")
width = the_rock.get_width()
height = the_rock.get_height()

window = image.ImageWin(width, height)
the_rock.draw(window)

for x in range(width):
    for y in range(height):
        this_pixel = the_rock.get_pixel(x, y)

        r = this_pixel.get_red()
        g = this_pixel.get_green()
        b = this_pixel.get_blue()

        if r <= 50 and g <= 50 and b <= 50:
            new_red = 50
            new_green = 140
            new_blue = 210
        else:
            new_red = r + 100
            new_green = g
            new_blue = b


        new_pixel = image.Pixel(new_red, new_green, new_blue)
        the_rock.set_pixel(x, y, new_pixel)

    the_rock.draw(window)
