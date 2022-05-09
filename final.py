
from multiprocessing.reduction import duplicate
from pprint import pprint
import praw
import urllib
import cv2
from collections import Counter
import re
import linecache
import hashlib
import os
import splitter

# clears file test.json for rerun------------------------------
ffile = open('test.json','r+')
ffile.truncate()
ffile.close()
# -------------------------------------------------------------

reddit = praw.Reddit(client_id='zWjxaNEf5mFbowd8YZ0ytA',
                     client_secret='4-crbYnGfzYMG8n4ReyvSr_P07dXxA',
                     user_agent='<uniQue>',
                     username='',
                     password='')

POST_SEARCH_AMOUNT = 2000

file = open("txtxt.txt", "w")

f_final = open("sub_list.csv", "r")
img_notfound = cv2.imread('imageNF.png')
for line in f_final:
    sub = line.strip()
    subreddit = reddit.redditor(sub)

print(f"Starting {sub}!")

for submission in subreddit.top(limit=POST_SEARCH_AMOUNT):
    url = str(submission.url)
    print(url)
    file.write(url + '\n')
    
    # -----------------------------------------------------------------------------

output_file_path = "editedtxt.txt"
input_file_path = "txtxt.txt"

completed_lines_hash = set()

output_file = open(output_file_path, "w")
for line in open(input_file_path, "r"):
    hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()

    if hashValue not in completed_lines_hash:
        output_file.write(line)
        completed_lines_hash.add(hashValue)

output_file.close()


# to replace the extionsion
search_text = ".gifv"
replace_text = ".mp4"

with open(r'txtxt.txt', 'r') as file:
    data = file.read()
    data = data.replace(search_text, replace_text)

with open(r'txtxt.txt', 'w') as file:
    file.write(data)
    print("Text replaced")
# completed replacing extionsions
# --------------------------------------------------------------

# # to cut paste the redgif file

print("*******")

# redgif = "redgif"
with open('txtxt.txt') as input_data:
    for line in input_data:
        if "redgif" in line:
            print(line)
            f = open(r"temp_redgif.txt", "a")
            f.write(line)
            f.close()


lines_seen = set()  # holds lines already seen
outfile = open('redgif.txt', "w")
infile = open('temp_redgif.txt', "r")
print ("The file temp_redgif.txt is as follows")
for line in infile:
    print (line)
    if line not in lines_seen:  # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()






# file.close


file.flush()
file.close





# --------------------------------------------------------------------

# to del redgif from txtxt.txt

# with open("txtxt.txt", "r+") as input:
#     with open("temp_txt.txt", "w+") as output:
#         # iterate all lines from file
#         for line in input:
#             # if text matches then don't write it
#             if line.strip("\n") != "text to delete":
#                 output.write(line)

# # replace file with original name
# os.replace('temp_txt.txt', 'txtxt.txt')
