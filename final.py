import praw
import os
import cv2
import hashlib

reddit = praw.Reddit(client_id='zWjxaNEf5mFbowd8YZ0ytA',
                     client_secret='4-crbYnGfzYMG8n4ReyvSr_P07dXxA',
                     user_agent='<uniQue>',
                     username='',
                     password='')

POST_SEARCH_AMOUNT = 20000

# read the subreddits from sub_list.csv
with open("sub_list.csv", "r") as f_subreddits:
    for sub in f_subreddits:
        sub = sub.strip()
        subreddit = reddit.redditor(sub)

        # create a folder with the subreddit name
        folder_path = os.path.join(".", sub)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        print(f"Scraping data for {sub}...")

        # create a file with the subreddit name to store the scraped data
        file_path = os.path.join(folder_path, f"{sub}.txt")
        with open(file_path, "w") as f_data:
            for submission in subreddit.top(limit=POST_SEARCH_AMOUNT):
                if hasattr(submission, 'url'):
                    url = str(submission.url)
                    print(url)
                    f_data.write(url + '\n')

        # remove duplicates and replace extension
        print(f"Cleaning data for {sub}...")
        completed_lines_hash = set()
        input_file_path = file_path
        output_file_path = os.path.join(folder_path, f"cleaned_{sub}.txt")

        with open(output_file_path, "w") as output_file:
            with open(input_file_path, "r") as input_file:
                for line in input_file:
                    hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()

                    if hashValue not in completed_lines_hash:
                        output_file.write(line)
                        completed_lines_hash.add(hashValue)

        # replace extension from gifv to mp4
        search_text = ".gifv"
        replace_text = ".mp4"

        with open(output_file_path, 'r') as file:
            data = file.read()
            data = data.replace(search_text, replace_text)

        with open(output_file_path, 'w') as file:
            file.write(data)

        # extract redgif URLs
        print(f"Extracting redgif URLs for {sub}...")
        with open(output_file_path, 'r') as input_file, open(os.path.join(folder_path, f"redgif_{sub}.txt"), "w") as output_file:
            lines_seen = set()  # holds lines already seen
            for line in input_file:
                if "redgif" in line and line not in lines_seen:
                    print(line)
                    output_file.write(line)
                    lines_seen.add(line)

print("Data scraping completed successfully!")
