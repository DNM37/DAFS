
import os

file_name = 'AndromedaENCODED.txt'
file_stats = os.stat(file_name)

filesize = (file_stats.st_size/(1024**2))

chunks = filesize%25

chunksize = filesize//24
print ((chunksize + 1))



