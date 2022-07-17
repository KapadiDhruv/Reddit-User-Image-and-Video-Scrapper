import json
import os 
from pymongo import MongoClient 
from os.path import exists
from colorama import Fore, Back, Style

original = r'sub_list.csv'

with open(original,'r') as firstfile: 
    for line in firstfile:
        path = ('to do - ' + line.lower())
        os.chdir(os.getcwd() + '\\' + path)
        # print(os.getcwd())
        # Making Connection
        myclient = MongoClient("mongodb+srv://dhruv:dhruv@cluster0.f37cf.mongodb.net/?retryWrites=true&w=majority") 
        
        # database 
        # give db name below after potty
        db = myclient['reddit']  
        
        # Created or Switched to collection 
        # names: GeeksForGeeks
        Collection1 = db[line + "_pics"]
        Collection2 = db[line + "_vid"]
        Collection3 = db[line + "_gyfcat"]
        Collection4 = db[line + "_Gallery_Links".lower()]
        Collection5 = db[line + "_imgur_album".lower()]


        if(exists('pics.json')):
            # Loading or Opening the json file
            with open('pics.json') as file:
                file_data = json.load(file)
                
            # Inserting the loaded data in the Collection
            # if JSON contains data more than one entry
            # insert_many is used else inser_one is used
            if isinstance(file_data, list):
                Collection1.insert_many(file_data)  
                print(Back.GREEN +'pics.json uploaded in mysql Database')
                print(Style.RESET_ALL)

            else:
                Collection1.insert_one(file_data)
        else:
            print(Back.RED + 'No pics.json file found to upload on Database')
            print(Style.RESET_ALL)


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
                print(Back.GREEN +'vid.json uploaded in mysql Database')
                print(Style.RESET_ALL)
            else:
                Collection2.insert_one(file_data)
        else:
            print(Back.RED + 'No vid.json file found to upload on Database')
            print(Style.RESET_ALL)


        # gyfcat
        if(exists('gyfcat_test.json')):
            # Loading or Opening the json file
            with open('gyfcat_test.json') as file:
                file_data = json.load(file)
                
            # Inserting the loaded data in the Collection
            # if JSON contains data more than one entry
            # insert_many is used else inser_one is used
            if isinstance(file_data, list):
                Collection3.insert_many(file_data)  
                print(Back.GREEN +'gyfcat.json uploaded in mysql Database')
                print(Style.RESET_ALL)
            else:
                Collection3.insert_one(file_data)
        else:
            print(Back.RED + 'No gyfcat.json file found to upload on Database')
            print(Style.RESET_ALL)



        # gallery
        if(exists('Gallery_Links.json')):
            # Loading or Opening the json file
            with open('Gallery_Links.json') as file:
                file_data = json.load(file)
                
            # Inserting the loaded data in the Collection
            # if JSON contains data more than one entry
            # insert_many is used else inser_one is used
            if isinstance(file_data, list):
                Collection4.insert_many(file_data) 
                print(Back.GREEN +'Gallery_Links.json uploaded in mysql Database')
                print(Style.RESET_ALL) 
            else:
                Collection4.insert_one(file_data)
        else:
           print(Back.RED + 'No Gallery_Links.json file found to upload on Database')
           print(Style.RESET_ALL)



        # imgur_album
        if(exists('imgur_album.json')):
            # Loading or Opening the json file
            with open('imgur_album.json') as file:
                file_data = json.load(file)
                
            # Inserting the loaded data in the Collection
            # if JSON contains data more than one entry
            # insert_many is used else inser_one is used
            if isinstance(file_data, list):
                Collection5.insert_many(file_data) 
                print(Back.GREEN +'imgur_album.json uploaded in mysql Database')
                print(Style.RESET_ALL) 
            else:
                Collection5.insert_one(file_data)
        else:
           print(Back.RED + 'No imgur_album.json file found to upload on Database')
           print(Style.RESET_ALL)





