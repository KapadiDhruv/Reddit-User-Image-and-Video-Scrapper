import csv
import os
import re

with open('sub_list.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        username = row[0]
        file_path = f"{username}/cleaned_{username}.txt"
        with open(f"{username}/{username}.txt", 'r') as file1, open(file_path, 'w') as file2:
            for line in file1:
                if not re.match(r'^https?://(v3\.)?(www\.)?redgifs\.com/watch/', line):
                    file2.write(line)
