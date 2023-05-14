# with open('txtxt.txt', 'r') as unedited_redgif:
#     with open('redgif.txt','w') as edited_redgif:
#         for line in unedited_redgif:
#             if "redgif" in line:
#                 edited_redgif.write(line)

# with open('redgif.txt', 'r') as f:
#     lst = []
#     for line in f:
#         line = line.replace('https://redgifs.com/watch/', '')
#         line = line.replace('https://www.redgifs.com/watch/', '')
#         line = line.replace('http://redgifs.com/watch/', '')
#         line = line.replace('http://www.redgifs.com/watch/', '')
#         line = line.replace('https://v3.redgifs.com/watch/', '')
#         line = line.replace('http://v3.redgifs.com/watch/', '')
#         lst.append(line)

# with open('redgif.txt', 'w') as f:
#     for line in lst:
#         f.write(line)
#         print(line)
import os
import csv

with open('sub_list.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        username = row[0]
        folder_path = f"{username}/"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        with open(f"{folder_path}onlyredgif_{username}.txt", 'w') as edited_redgif:
            with open(f"{folder_path}redgif_{username}.txt", 'r') as unedited_redgif:
                for line in unedited_redgif:
                    if "redgif" in line:
                        edited_redgif.write(line)

        with open(f"{folder_path}redgif_{username}.txt", 'r') as f:
            lst = []
            for line in f:
                line = line.replace('https://redgifs.com/watch/', '')
                line = line.replace('https://www.redgifs.com/watch/', '')
                line = line.replace('http://redgifs.com/watch/', '')
                line = line.replace('http://www.redgifs.com/watch/', '')
                line = line.replace('https://v3.redgifs.com/watch/', '')
                line = line.replace('http://v3.redgifs.com/watch/', '')
                line = line.replace('https://i.redgifs.com/i/', '')
                line = line.replace('http://i.redgifs.com/i/', '')
                lst.append(line)

        with open(f"{folder_path}onlyredgif_{username}.txt", 'w') as f:
            for line in lst:
                f.write(line)
                print(line)
