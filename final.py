import praw
import cv2
import hashlib

# clears file test.json for rerun
with open('test.json', 'w'):
    pass

reddit = praw.Reddit(client_id='zWjxaNEf5mFbowd8YZ0ytA',
                     client_secret='4-crbYnGfzYMG8n4ReyvSr_P07dXxA',
                     user_agent='<uniQue>',
                     username='',
                     password='')

POST_SEARCH_AMOUNT = 2500

f_final = open("sub_list.csv", "r")

for line in f_final:
    sub = line.strip()
    subreddit = reddit.redditor(sub)

    print(f"Starting {sub}!")

    with open("txtxt.txt", "w") as file:
        for submission in subreddit.top(limit=POST_SEARCH_AMOUNT):
            if hasattr(submission, 'url'):
                url = str(submission.url)
                print(url)
                file.write(url + '\n')

# Eliminate duplicates and write to output file
completed_lines_hash = set()
output_file_path = "editedtxt.txt"
input_file_path = "txtxt.txt"

with open(output_file_path, "w") as output_file:
    with open(input_file_path, "r") as input_file:
        for line in input_file:
            hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()

            if hashValue not in completed_lines_hash:
                output_file.write(line)
                completed_lines_hash.add(hashValue)

# Replace extension
search_text = ".gifv"
replace_text = ".mp4"

with open(r'txtxt.txt', 'r') as file:
    data = file.read()
    data = data.replace(search_text, replace_text)

with open(r'txtxt.txt', 'w') as file:
    file.write(data)
    print("Text replaced")

# Extract redgif URLs
with open('txtxt.txt', 'r') as input_file, open('redgif.txt', "w") as output_file:
    lines_seen = set()  # holds lines already seen
    for line in input_file:
        if "redgif" in line and line not in lines_seen:
            print(line)
            output_file.write(line)
            lines_seen.add(line)
