import os
import re


search_text = ".gifv"
replace_text = ".mp4"

search_text1 = ".gif"
replace_text1 = ".mp4"

with open(r'txt.txt', 'r') as file:
    data = file.read()
    data = data.replace(search_text, replace_text)

with open(r'txt.txt', 'w') as file:
    file.write(data)
    print("Text replaced")

# with open(r'txtxt.txt', 'r') as file:
#     data = file.read()
#     data = data.replace(search_text1, replace_text1)

# with open(r'txtxt.txt', 'w') as file:
#     file.write(data)
#     print("Text replaced")



