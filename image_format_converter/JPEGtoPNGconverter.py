import os
import sys
from os import listdir
from os import path

from PIL import Image

# Grab the input & output folders
input_dir = sys.argv[1]
output_dir = sys.argv[2]

# Create the output folder if it doesn't exist
if not path.exists(output_dir):
    os.makedirs(output_dir)

# Transform all JPEG files to PNG
for filename in listdir(input_dir):
    clean_name = path.splitext(filename)[0]
    img = Image.open(f'{input_dir}{filename}')
    img.save(f'{output_dir}/{clean_name}.png', 'png')
    print('all done!')
