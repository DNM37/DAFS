import file_to_text
import json

source = 'Andromeda.png'
output = 'AndromedaENCODED.txt'

file_registry = 'file_reg.json'

temp_hash = {}


storage_name = output[:-4]

destination_file = file_to_text.file_to_text(source, output)

temp_hash[storage_name] = file_to_text.file_segmentation(output, storage_name)


with open(file_registry, 'w') as file:  #file registry is the dictionary containing instructions of how to rebuidl the files
    # Serialize the updated dictionary to JSON and write it to the file
    json.dump(temp_hash, file)

