import image   #This is the cs20-image module

the_image = image.Image("rooster.jpg")
width = the_image.get_width()
height = the_image.get_height()

canvas = image.ImageWin(width, height)

the_image.draw(canvas) # This is optional, if you are using image processing to change an image, you can see the image as it is changing. This doesn't have to be here.

for x in range(width):
    for y in range(height):
        current_pixel = the_image.get_pixel(x, y) #specifies that the pixel we want is located at x, for the x value in the for loop, and the y from the for y loop
        
        red = current_pixel.getRed()
        green = current_pixel.getGreen()
        blue = current_pixel.getBlue()

        brighter_pixel = image.Pixel(red + 10, green + 10, blue + 10)

        the_image.set_pixel(x, y, brighter_pixel)
    the_image.draw(canvas)# Moving this back so the pixels are changed column by column
