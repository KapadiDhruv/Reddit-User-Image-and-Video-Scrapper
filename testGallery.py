import os
import subprocess

from_file = 'onlygallery.txt'
to_file = 'finalgallery.txt'

with open(from_file, "r") as file:
    gallery = []
    for line in file:
        sub = 'https://www.reddit.com/gallery/' + line.strip()
        print(sub)
        url = 'gallery-dl -g '
        r = url + sub
        # capture output of command
        result = subprocess.run(r, shell=True, capture_output=True)
        # check if command was successful
        if result.returncode == 0:
            # append output to gallery list
            gallery.append(result.stdout.decode())

# write gallery list to finalgallery.txt
with open(to_file, 'w') as f:
    f.write('\n'.join(gallery))
