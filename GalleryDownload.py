import os
import csv
import praw

with open("sub_list.csv", "r") as f_subreddits:
    for sub in f_subreddits:
        sub = sub.strip()
        username = sub

        # Get username from sub_list.csv and set paths
        input_file_path = f'{username}/cleaned_{username}.txt'
        output_file_path = f'{username}/onlygallery_{username}.txt'

        # FILTERING OUT URL LINES CONTAINING "GALLERY" FROM THE INPUT FILE AND WRITING THEM TO THE OUTPUT FILE
        with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
            for line in input_file:
                if 'gallery' in line:
                    output_line = line.replace('https://www.reddit.com/gallery/', '')
                    output_file.write(output_line)
                    print(output_line)
