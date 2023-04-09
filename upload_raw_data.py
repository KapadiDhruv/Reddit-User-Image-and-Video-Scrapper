import os, shutil
import csv,json
from pymongo import MongoClient 
from os.path import exists
from colorama import Fore, Back, Style
from telnetlib import GA
import mysql.connector
from importlib.resources import path
import pandas as pd
from sqlalchemy import create_engine, engine



source = r'txtxt.txt'
dest = r'temp_txtxt.txt'

shutil.copy(source,dest)

# to change from csv to json 
def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python3 dict
        for row in csvReader: 
            #add this python3 dict to json array
            jsonArray.append(row)
  
    #convert python3 jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
          

line = 'url'
with open('temp_txtxt.txt', 'r+') as file: 
    file_data = file.read() 
    file.seek(0, 0) 
    file.write(line + '\n' + file_data) 


my_file = "temp_txtxt.txt"
base = os.path.splitext(my_file)[0]
os.rename(my_file, base + '.csv')


# to convert the file from csv to json
csvFilePath = r'temp_txtxt.csv'
jsonFilePath = r'txtxt.json'

csv_to_json(csvFilePath, jsonFilePath)

# ---------------------------------------------------------------------------------------------------------
# delete the csv file

os.remove('temp_txtxt.csv')

# -----------------------------------------------------------------------------------------------------------

# transfer to mongo

original = r'sub_list.csv'

with open(original,'r') as firstfile: 
    for line in firstfile:
        user_name = line
        path = ('txtxt.json')
        # Making Connection
        myclient = MongoClient("mongodb+srv://dhruv:dhruv@cluster0.f37cf.mongodb.net/?retryWrites=true&w=majority") 
        
        # database 
        # give db name below after potty
        db = myclient['reddit']  
        
        # Created or Switched to collection 
        # names: GeeksForGeeks
        Collection1 = db[user_name + "_raw"]
 
        
        with open('txtxt.json') as file:
            file_data = json.load(file)
            
        # Inserting the loaded data in the Collection
        # if JSON contains data more than one entry
        # insert_many is used else inser_one is used
        if isinstance(file_data, list):
            Collection1.insert_many(file_data)  
            print(Back.GREEN + user_name + '_raw json uploaded in MONGO Database')
            print(Style.RESET_ALL)

        else:
            Collection1.insert_one(file_data)
#-------------------------------------------------------------------------------------------------------------------------------------------

#  transfer to mysql

# 1. create table

f_final = open("sub_list.csv", "r")
for line in f_final:
    user_name = line.strip()
    raw_qry =  f"""CREATE TABLE `reddit`.`{user_name + '_raw'}` (`id` INT NOT NULL AUTO_INCREMENT,`url` VARCHAR(45) NULL,PRIMARY KEY (`id`));"""
    print(raw_qry)       

    # connecting to the database
    dataBase = mysql.connector.connect(
                        host = "localhost",
                        user = "root",
                        passwd = "dhruv",
                        database = "reddit" ) 
    
    # preparing a cursor object
    cursorObject = dataBase.cursor()
    
    # creating table 
    user_name_raw           = raw_qry

    
    # table created
    cursorObject.execute(user_name_raw) 
  
    # disconnecting from server
    dataBase.close()
# -----------------------------------------

# 2. push to mysql table

original = r'sub_list.csv'

with open(original,'r') as firstfile: 
    for user_name in firstfile:
        print(os.getcwd())

        #  pics
        engine = create_engine('mysql+pymysql://root:dhruv@localhost/reddit')
        pics = os.path.join(os.getcwd() + '/txtxt.json')

        df = pd.read_json(pics)
        table_name = (user_name + '_raw').lower()
        # database name always save in db in small letters
        df.to_sql(table_name,con=engine,if_exists='replace')

        print(Back.GREEN + user_name + '_raw json uploaded in MYSQL Database')
        print(Style.RESET_ALL)

# -----------------------------------------------------------------------------------------------------------------
print('')
#  delete the txtxt.json file
os.remove('txtxt.json')
