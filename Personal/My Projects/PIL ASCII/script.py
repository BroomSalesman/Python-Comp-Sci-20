import PIL.Image


#ascii characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


# resize image according to a new width
def resize_image(image, new_width = 100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height)



# convert each pixel to grayscale


# convert pixels to a string of ASCII characters


def main():
    path = input("Enter a valid pathanem to an image:\n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "is not a valid pathname to an image")
