import os
import subprocess

with open("sub_list.csv", "r") as f_subreddits:
    for sub in f_subreddits:
        sub = sub.strip()
        username = sub
    from_file = f'{username}/onlygallery_{username}.txt'
    to_file = f'{username}/cleaned_gallerylinks_{username}.txt'

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
                gallery.append(result.stdout.decode().rstrip())

    # write gallery list to finalgallery.txt
    with open(to_file, 'w') as f:
        f.write('\n'.join(gallery))

    with open(to_file, 'r') as file:
        lines = file.readlines()

    with open(to_file, 'w') as file:
        for line in lines:
            if line.strip():
                file.write(line)