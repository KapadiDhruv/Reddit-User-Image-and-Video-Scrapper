import re

with open("sub_list.csv", "r") as f_subreddits:
    for sub in f_subreddits:
        sub = sub.strip()
        username = sub

    with open(f"{username}/cleaned_{username}.txt", "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if not re.match("^http://imgur.com/a/", line):
                file.write(line)
        file.truncate()
