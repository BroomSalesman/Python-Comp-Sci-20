import image

img = image.Image("giraffe.jpg")
width = img.get_width()
height = img.get_height()

win = image.ImageWin(width, height)
img.draw(win)

for x in range(width//2):
    for y in range(height):
        this_pixel = img.get_pixel(x, y)


        img.set_pixel(width// 2 + x, y, this_pixel)

        img.draw(win)
