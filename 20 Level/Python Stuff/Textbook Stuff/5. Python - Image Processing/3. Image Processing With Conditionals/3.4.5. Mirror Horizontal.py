import image
import time

the_rock = image.Image("the_rock.png")
width = the_rock.get_width()
height = the_rock.get_height()

win = image.ImageWin(width, height)
the_rock.draw(win)

# Going to use to reverse the items of the list
x_values = []

x_values.append(x for x in range(width))

while len(x_values) != len(x_values)//2:
    for i in x_values:
        x_values.remove(i)

print(x_values)


for x in range(width):
    for y in range(height):
        this_pixel = the_rock.get_pixel(x, y)

        r = this_pixel.getRed()
        g = this_pixel.getGreen()
        b = this_pixel.getBlue()

        if x <= width//2: # I still don't understand why it didn't mirror the left side when x > width/2
            the_rock.set_pixel(width//2 + (width//2 - x), y, this_pixel)
        else:
            new_pixel = image.Pixel(255 - r, 255 - g, 255 - b)
            the_rock.set_pixel(x, y, new_pixel)

the_rock.draw(win)

time.sleep(3)
