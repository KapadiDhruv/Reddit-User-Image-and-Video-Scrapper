# with open('txtxt.txt', 'r') as unedited_redgif, open('only_imgur_album.txt','w+') as edited_redgif:
#     for line in unedited_redgif:
#         if "imgur.com/a/" in line:
#             print(line)
#             edited_redgif.write(line)

# words_to_replace = ['http://imgur.com/a/', 'https://imgur.com/a/', 'https://m.imgur.com/a/', 'http://m.imgur.com/a/']

# with open('only_imgur_album.txt','r') as f:
#     lst = []
#     for line in f:
#         for word in words_to_replace:
#             if word in line:
#                 line = line.replace(word,'')
#         lst.append(line)

# with open('only_imgur_album.txt','w') as f:
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

        with open(f"{folder_path}{username}.txt", 'r') as unedited_redgif, open(f"{folder_path}only_imgur_album_{username}.txt",'w+') as edited_redgif:
            for line in unedited_redgif:
                if "imgur.com/a/" in line:
                    print(line)
                    edited_redgif.write(line)

        words_to_replace = ['http://imgur.com/a/', 'https://imgur.com/a/', 'https://m.imgur.com/a/', 'http://m.imgur.com/a/']

        with open(f"{folder_path}only_imgur_album_{username}.txt",'r') as f:
            lst = []
            for line in f:
                for word in words_to_replace:
                    if word in line:
                        line = line.replace(word,'')
                lst.append(line)

        with open(f"{folder_path}only_imgur_album_{username}.txt",'w') as f:
            for line in lst:
                f.write(line)
                print(line)
