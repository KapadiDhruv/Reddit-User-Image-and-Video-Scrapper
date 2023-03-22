import re

with open('txtxt.txt', 'r') as file_in, open('txt.txt', 'w') as file_out:
    for line in file_in:
        if not re.match("^https://gfycat.com", line):
            print(line)
            file_out.write(line)
