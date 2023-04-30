import json
import os 
from pymongo import MongoClient 
from os.path import exists
from dotenv import load_dotenv
load_dotenv()

mongo_url = os.environ.get('MONGO_URL')

with open("sub_list.csv", "r") as f_subreddits:
    for sub in f_subreddits:
        sub = sub.strip()
        username = sub
    myclient = MongoClient(f"{mongo_url}") 
    # myclient = MongoClient("mongodb://localhost:27017") 

    db = myclient['reddit']  
    Collection = db[f"{username.lower()}"]

    with open(f'{username}/file_links.json') as file:
        file_data = json.load(file)

        if isinstance(file_data, list):
                Collection.insert_many(file_data)  

        else:
            Collection.insert_one(file_data)