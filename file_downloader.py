import os
import itertools
import shutil
from PIL import Image
import base64
import io

import json

# File path where the dictionary is saved
file_path = 'file_reg.json'

# Load the dictionary from the file
with open(file_path, 'r') as file:
    loaded_dict = json.load(file)

# Access the data from the loaded dictionary
print(loaded_dict)

current_files = loaded_dict['AndromedaENCODED'][0]

output_txt_file = 'AndromedaENCODED.txt'

output_file = 'AndromedaRECONSTRUCTED.png'


def combine(chunks, output_txt_file):
    combined_text = ""
    for chunk_file in chunks:
        with open(chunk_file, "r") as file:
            chunk_text = file.read()
            combined_text += chunk_text
    
    with open(output_txt_file, "w") as out_file:
        out_file.write(combined_text)

def decode_text_to_image(encoded_text):
    # Add padding if necessary
    padded_encoded_text = encoded_text + '=' * (-len(encoded_text) % 4)
    decoded_bytes = base64.b64decode(padded_encoded_text)
    image = Image.open(io.BytesIO(decoded_bytes))
    return image

combine(current_files, output_txt_file)

with open(output_txt_file, "r") as file:
    encoded_text = file.read()

for image in current_files:
    os.remove(image)
image = decode_text_to_image(encoded_text)

image.save(output_file, "PNG")
os.remove(output_txt_file)