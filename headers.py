from asyncore import write
from textwrap import indent
import requests
import json
import os
import pandas as pd
import requests
import sys
import string

file = open('redgif.txt',"r+")
for line in file:
    sub = line.strip()
    # print(sub)
    url = "https://api.redgifs.com/v2/gifs/"
    term = sub
    # print(url + term)
    r = requests.get(url + term)
    print(r.json())
    with open('json.json', 'w') as f:
        f.write(json.dumps(r.json(), indent = 1))

    json_file = open('json.json', 'r')
    edited_file = open('test.json','a')

    for line in json_file:
        if "hd" in line:
            print(line)
            edited_file.write(line)

    json_file.close()
    edited_file.close()
print("-----------------------------------------------")

search_text = '"hd": "'
search_text1 = '",'
replace_text = " "

with open(r'test.json', 'r') as file:
    data = file.read()
    data = data.replace(search_text, replace_text)
    data = data.replace(search_text1, replace_text)

with open(r'test.json', 'w') as file:
    file.write(data)
    print("Text replaced")
        
    

# word_1 = '"hd": "'
# word_2 = '",'
# f_file = "test.json"
# delete_list = [word_1,word_2]
# with open(f_file,"r+") as fin, open(f_file, "w+") as fout:
#     for line in fin:
#         for word in delete_list:
#             line = line.replace(word, "")
#         fout.write(line)
        
# f_file.close()






