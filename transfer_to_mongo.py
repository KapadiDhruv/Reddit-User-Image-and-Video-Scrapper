import json
import os 
from pymongo import MongoClient 
from os.path import exists

original = r'sub_list.csv'

with open(original,'r') as firstfile: 
    for line in firstfile:
        path = ('to do - ' + line)
        os.chdir(os.getcwd() + '\\' + path)
        # print(os.getcwd())
        # Making Connection
        myclient = MongoClient("mongodb+srv://dhruv:dhruv@cluster0.f37cf.mongodb.net/?retryWrites=true&w=majority") 
        
        # database 
        db = myclient[line]
        
        # Created or Switched to collection 
        # names: GeeksForGeeks
        Collection1 = db["pics"]
        Collection2 = db["vid"]
        Collection3 = db["gyfcat"]
        Collection4 = db["Gallery_Links"]


        if(exists('pics.json')):
            # Loading or Opening the json file
            with open('pics.json') as file:
                file_data = json.load(file)
                
            # Inserting the loaded data in the Collection
            # if JSON contains data more than one entry
            # insert_many is used else inser_one is used
            if isinstance(file_data, list):
                Collection1.insert_many(file_data)  
            else:
                Collection1.insert_one(file_data)
        else:
            print("no pics files")


        # vids
        if(exists('vid.json')):
            # Loading or Opening the json file
            with open('vid.json') as file:
                file_data = json.load(file)
                
            # Inserting the loaded data in the Collection
            # if JSON contains data more than one entry
            # insert_many is used else inser_one is used
            if isinstance(file_data, list):
                Collection2.insert_many(file_data)  
            else:
                Collection2.insert_one(file_data)
        else:
            print("no vid files")

        # gyfcat
        if(exists('gyfcat.json')):
            # Loading or Opening the json file
            with open('gyfcat.json') as file:
                file_data = json.load(file)
                
            # Inserting the loaded data in the Collection
            # if JSON contains data more than one entry
            # insert_many is used else inser_one is used
            if isinstance(file_data, list):
                Collection3.insert_many(file_data)  
            else:
                Collection3.insert_one(file_data)
        else:
            print("no gyfcat files")


        # gallery
        if(exists('Gallery_Links.json')):
            # Loading or Opening the json file
            with open('gallery.json') as file:
                file_data = json.load(file)
                
            # Inserting the loaded data in the Collection
            # if JSON contains data more than one entry
            # insert_many is used else inser_one is used
            if isinstance(file_data, list):
                Collection4.insert_many(file_data)  
            else:
                Collection4.insert_one(file_data)
        else:
            print("no gallery files")




