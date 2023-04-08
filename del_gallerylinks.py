import os

with open("sub_list.csv", "r") as f_subreddits:
    for sub in f_subreddits:
        sub = sub.strip()
        username = sub

        # Open cleaned file and remove lines containing "gallery"
        with open(f"{username}/cleaned_{username}.txt", "r+") as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                # Check if line contains "gallery"
                if "gallery" not in line:
                    # If not, write line to file
                    file.write(line)
            file.truncate()
