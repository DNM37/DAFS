import shutil
import base64
import itertools
import os
def file_to_text(source, output):
    with open(source, "rb") as img_file:
        img_bytes = img_file.read()
        encoded_bytes = base64.b64encode(img_bytes)
        encoded_string = encoded_bytes.decode('utf-8')  # Convert bytes to string
        
        # Write encoded text to file
        with open(output, "w") as out_file:
            out_file.write(encoded_string)



def file_segmentation(destination_file, source):
    filenames = []
    with open(destination_file, "r") as file:
        
        encoded_text = file.read()
        total_length = len(encoded_text)
        

        iters = how_many_times(destination_file)

        chunk_size = total_length // iters

        chunk_size = int(chunk_size)

        for i in range(int(iters)):
            start_index = i * chunk_size
            end_index = (i + 1) * chunk_size
            if end_index >= total_length:
                end_index = total_length
            else:
                end_index = (i + 1) * chunk_size    # For the last chunk
                
            chunk = encoded_text[start_index:end_index]
            
            output_file = f"{source}_{i + 1}.txt"
            filenames.append(output_file)
            with open(output_file, "w") as out_file:
                out_file.write(chunk)

    os.remove(destination_file)
    return [filenames]
    

def how_many_times(file):
    file_stats = os.stat(file)

    filesize = (file_stats.st_size/(1024**2))

    chunksize = filesize//24

    return (chunksize + 1)
#then divide amount of lines in the file by the amount of chunks
#when i have the amount of chunks in the file, then i subtract that from the file size, then divide by the chunk size (25mb ) this will give the amount of lines to write. 
