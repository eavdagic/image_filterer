from PIL import Image
import sys
import os
from datetime import datetime

def main(img_path):
    img = Image.open(img_path)
   
    file_name = create_img_name(img_path)
    img_pixels = img.load()

    img_height = img.size[0]
    img_width = img.size[1]

    for i in range(img_height):
        for j in range(img_width):
            r, g, b = img.getpixel((i,j))

            img_pixels[i,j] = greenify(r, g, b)

    img.save(file_name + '.jpg')
    print('image created with name: {}.jpg'.format(file_name))

def greenify(r, g, b):
    return (r, g, b-100) 

def create_img_name(path):
    if type(path) is str and len(path) > 0:
        dt_string = datetime.now().strftime('%y%m%d%I%M%S')
        name_from_path = os.path.basename(path).split('.')[0]
        name = name_from_path + dt_string 
        
        return name

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print('Missign image path argument')
