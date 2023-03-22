import re

with open('txtxt.txt', 'r') as file1, open('txt.txt', 'w') as file2:
    for line in file1:
        if not re.match(r'^https?://(v3\.)?(www\.)?redgifs\.com/watch/', line):
            print(line)
            file2.write(line)
