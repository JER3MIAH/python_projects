import os
import sys
from PIL import Image

# Create the output folder if it doesn't exist
# loop through allfiles in the input folder
# check if the file is a jpg image
# open the image using pillow
# construct the output filepath with the same filename but with png extension
# save the image as png in the output folder


def image_converter(folder_name, new_folder_name):
    os.makedirs(new_folder_name, exist_ok=True)
    for filename in os.listdir(folder_name):
        file_path = os.path.join(folder_name, filename)

        if filename.lower().endswith('.jpg'):
            image = Image.open(file_path)

            new_file_path = os.path.join(new_folder_name, os.path.splitext(filename)[0] + '.png')
            image.save(new_file_path, 'png')
            print(f'converted {filename} to PNG')

        else:
            print(f'Folder {folder_name} does not exist')


folder_name1 = sys.argv[1]
new_folder_name2 = sys.argv[2]
image_converter(folder_name1, new_folder_name2)
