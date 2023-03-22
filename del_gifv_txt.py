import os

search_replace_list = [
    (".gifv", ".mp4"),
    (".gif", ".mp4")
]

for filename in ['txt.txt', 'txtxt.txt']:
    with open(filename, 'r') as file:
        data = file.read()
        for search_text, replace_text in search_replace_list:
            data = data.replace(search_text, replace_text)
    with open(filename, 'w') as file:
        file.write(data)
    print(f"Text replaced in {filename}")
