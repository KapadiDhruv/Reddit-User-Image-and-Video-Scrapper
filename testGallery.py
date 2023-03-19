import os
import subprocess

from_file = 'onlygallery.txt'
to_file = 'finalgallery.txt'

file = open(from_file, "r+")
gallery = []
for line in file:
    sub = 'https://www.reddit.com/gallery/' + line.strip()
    print(sub)
    url = 'gallery-dl -g '
    r = url + sub
    # capture output of command
    result = subprocess.check_output(r, shell=True)
    # append output to gallery list
    gallery.append(result.decode())
    
# write gallery list to finalgallery.txt
with open(to_file, 'w') as f:
    f.write('\n'.join(gallery))
