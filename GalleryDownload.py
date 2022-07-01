from asyncore import write
from os import truncate
from RedDownloader import RedDownloader
from requests import delete
import string
import random
import praw
# RedDownloader.Download(url, destination="D:/Pictures/")
reddit = praw.Reddit(client_id='zWjxaNEf5mFbowd8YZ0ytA',
                     client_secret='4-crbYnGfzYMG8n4ReyvSr_P07dXxA',
                     user_agent='<uniQue>',
                     username='',
                     password='')

# GETTING ALL THE GALLERY URL'S LAST TERM 
f = open('txtxt.txt','r')
a = ['https://www.reddit.com/gallery/']
lst = []
for line in f:
    for word in a:
        if word in line:  
            line = line.replace(word,'')
    lst.append(line)
f.close()
f = open('onlygallery.txt','w+')
for line in lst:
    f.write(line)
f.close()



with open("onlygallery.txt", "r+") as f:
    # First read the file line by line
    lines = f.readlines()

    # Go back at the start of the file
    f.seek(0)

    # Filter out and rewrite lines
    for line in lines:
        if not line.startswith('htt'):
            f.write(line)

    # Truncate the remaining of the file
    f.truncate()

 

