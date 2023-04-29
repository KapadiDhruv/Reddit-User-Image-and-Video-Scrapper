import json
import os 
from pymongo import MongoClient 
from os.path import exists
from colorama import Fore, Back, Style


with open("sub_list.csv", "r") as f_subreddits:
    for sub in f_subreddits:
        sub = sub.strip()
        username = sub
    # myclient = MongoClient("mongodb+srv://dhruv:dhruv@cluster0.f37cf.mongodb.net/?retryWrites=true&w=majority") 
    myclient = MongoClient("mongodb://localhost:27017") 

    db = myclient['reddit']  
    Collection = db[f"{username.lower()}"]

    with open(f'{username}/file_links.json') as file:
        file_data = json.load(file)

        if isinstance(file_data, list):
                Collection.insert_many(file_data)  
                print(Back.GREEN +'pics.json uploaded in mysql Database')
                print(Style.RESET_ALL)

        else:
            Collection.insert_one(file_data)