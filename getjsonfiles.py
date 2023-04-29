import json

with open("sub_list.csv", "r") as f_subreddits:
    for sub in f_subreddits:
        sub = sub.strip()
        username = sub
    with open(f'{username}/cleaned_{username}.txt', 'r') as f:
        urls = f.readlines()

    data = {}

    for i, url in enumerate(urls):
        url = url.strip()
        filename = url.split('/')[-1]
        data[f"{i+1}_{filename}"] = url

    with open(f'{username}/cleaned_{username}.txt', 'w') as f:
        json.dump(data, f, indent=4)
