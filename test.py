import os 
with open("sub_list.csv", "r") as f_subreddits:
    for sub in f_subreddits:
        sub = sub.strip()
        username = sub
    os.system(f"gsutil -m cp -R {username} gs://my-homies-bucket1/Reddit")