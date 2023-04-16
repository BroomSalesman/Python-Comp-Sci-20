import requests
from PIL import Image
from io import BytesIO

search_term = input("Enter search term: ")
num_images = int(input("Enter number of images to download: "))
directory = input("Enter directory to save images: ")

url = "https://www.google.com/search?q={}&tbm=isch".format(search_term)
response = requests.get(url)

image_links = []
i = 0
while len(image_links) < num_images:
    if 'class="rg_i"' in response.text:
        split_text = response.text.split('class="rg_i"')
        for j in range(len(split_text)-1):
            image_link = split_text[j].split('"')[-2]
            if image_link.startswith("http") and not image_link.endswith(("gif", "GIF")):
                image_links.append(image_link)
                i += 1
                if i == num_images:
                    break
    if len(image_links) < num_images:
        response = requests.get(url+"&start="+str(i))

for index, link in enumerate(image_links):
    response = requests.get(link)
    image = Image.open(BytesIO(response.content))
    filename = "{}/{}_{}.jpg".format(directory, search_term, index+1)
    image.save(filename)

print("Images saved in directory:", directory)
