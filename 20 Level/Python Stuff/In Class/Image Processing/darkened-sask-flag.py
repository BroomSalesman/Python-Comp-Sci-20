
import os
import image


directory = os.path.dirname(os.path.abspath(__file__))
#sub_folder_path = os.path.join()
print("c:\\image")
for _ in os.listdir("c:\\Users\Labeeb & Menaal\\Desktop\Labeeb's Stuff\\Python-Comp-Sci-20\\Python Stuff\\In Class\\Image Processing\\images"):
    print(_)
    if _.endswith(".png") or _.endswith(".jpg"):
        img = image.Image(_)
        width = img.get_width()
        height = img.get_height()

        canvas =  image.ImageWin(width, height)
        img.draw(canvas)

        # Look at every pixel
        for x in range(width):
            for y in range(height):
                the_pixel = img.get_pixel(x, y)

                r = the_pixel.get_red()
                g = the_pixel.get_green()
                b = the_pixel.get_blue()

                new_pixel = image.Pixel(r - 50, g - 50, b - 50)

                img.set_pixel(x, y, new_pixel)

            img.draw(canvas)
