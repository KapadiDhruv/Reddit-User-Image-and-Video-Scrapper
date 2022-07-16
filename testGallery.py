import os
# https://github.com/mikf/gallery-dl

# pip3 install gallery-dl

from_file = 'onlygallery.txt'
to_file = 'finalgallery.txt'

file = open(from_file,"r+")
gallery = []
for line in file:
    sub = 'https://www.reddit.com/gallery/' + line.strip()
    print(sub)
    url = 'gallery-dl -g '
    r = url + sub
    # print(r)
    os.system(r)
    
