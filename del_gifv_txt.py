import os
import csv
search_replace_list = [
    (".gifv", ".mp4"),
    (".gif", ".mp4")
]
with open('sub_list.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        username = row[0]
        file_path = f"{username}/cleaned_{username}.txt"
        with open(file_path, 'r') as file:
            data = file.read()
            for search_text, replace_text in search_replace_list:
                data = data.replace(search_text, replace_text)
        with open(file_path, 'w') as file:
            file.write(data)
        print(f"Text replaced")

        