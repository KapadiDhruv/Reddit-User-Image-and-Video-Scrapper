from asyncore import write
from textwrap import indent
import requests
import json
import os
import pandas as pd
import requests
import sys
import string


# for gyfcat
print("*******")


with open('txtxt.txt') as input_data:
    for line in input_data:
        if "gfycat" in line:
            print(line)
            f = open(r"temp_gyfcat.txt", "a")
            f.write(line)
            f.close()


lines_seen = set()  # holds lines already seen
outfile = open('gyfcat.txt', "w")
infile = open('temp_gyfcat.txt', "r")
print ("The file temp_gyfcat.txt is as follows")
for line in infile:
    print (line)
    if line not in lines_seen:  # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()

# to delete some words
f = open('gyfcat.txt','r')
a = ['https://gfycat.com/']
lst = []
for line in f:
    for word in a:
        if word in line:
            line = line.replace(word,'')
    lst.append(line)
f.close()
f = open('gyfcat.txt','w')
for line in lst:
    f.write(line)
f.close()
# ----------------------------------------------------------------------------------------


file = open('gyfcat.txt',"r+")
for line in file:
    sub = line.strip()
    # print(sub)
    url = "https://api.gfycat.com/v1/gfycats/"
    term = sub
    # print(url + term)
    r = requests.get(url + term)
    print(r.json())
    with open('gyfcat_json.json', 'w') as f:
        f.write(json.dumps(r.json(), indent = 1))

    json_file = open('gyfcat_json.json', 'r')
    edited_file = open('gyfcat_test.json','a')

    for line in json_file:
        if "thumb100PosterUrl" in line:
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
        
    
# to delete some words

search_text = '"thumb100PosterUrl": "'
search_text1 = '-mobile'
replace_text = " "

with open(r'gyfcat_test.json', 'r') as file:
    data = file.read()
    data = data.replace(search_text, replace_text)
    data = data.replace(search_text1, replace_text)

with open(r'gyfcat_test.json', 'w') as file:
    file.write(data)
    print("Text replaced")


# 2nd time
search_text = '",'
search_text1 = 'thumbs'
search_text2 = ' .jpg'
replace_text = " "
replace_text1 = "giant"
replace_text2 = ".mp4"

with open(r'gyfcat_test.json', 'r') as file:
    data = file.read()
    data = data.replace(search_text, replace_text)
    data = data.replace(search_text1, replace_text1)
    data = data.replace(search_text2, replace_text2)

with open(r'gyfcat_test.json', 'w') as file:
    file.write(data)
    print("Text replaced")

        




