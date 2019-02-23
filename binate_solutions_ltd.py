import requests
import shutil

image_file = []
with open("images.txt","r",encoding='utf-8')as url_file:
    for image in url_file:
        image_file.append(image.rstrip("\n"))

def image_download(image_file):
    for store_image in image_file:
        req = requests.get(store_image,allow_redirects=False)
        open(store_image.split("/")[-1],'wb').write(req.content)
        shutil.move(store_image.split("/")[-1], 'Img/')

image_download(image_file)
