import string
import random
import praw

reddit = praw.Reddit(
    client_id='zWjxaNEf5mFbowd8YZ0ytA',
    client_secret='4-crbYnGfzYMG8n4ReyvSr_P07dXxA',
    user_agent='<uniQue>',
    username='',
    password=''
)

# GETTING ALL THE GALLERY URL'S LAST TERM 
with open('txtxt.txt', 'r') as f, open('onlygallery.txt', 'w') as output_file:
    gallery_urls = [line.replace('https://www.reddit.com/gallery/', '') for line in f if 'https://www.reddit.com/gallery/' in line]
    output_file.write('\n'.join(gallery_urls))

# FILTERING OUT NON-URL LINES FROM THE OUTPUT FILE
with open('onlygallery.txt', 'r+') as f:
    lines = f.readlines()
    filtered_lines = [line for line in lines if line.startswith('http')]
    f.seek(0)
    f.write(''.join(filtered_lines))
    f.truncate()
