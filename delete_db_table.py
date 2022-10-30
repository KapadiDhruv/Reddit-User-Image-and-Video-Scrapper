import mysql.connector
import os 
from pymongo import MongoClient 

print('hold on deleting the tables!')

user_name = "sevin7676"

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="dhruv",
  database="reddit"
)
myclient = MongoClient("mongodb+srv://dhruv:dhruv@cluster0.f37cf.mongodb.net/?retryWrites=true&w=majority") 
db = myclient['reddit']  


Collection1 = db[ user_name + "_pics" ]
Collection2 = db[ user_name + "_vid"]
Collection3 = db[ user_name + "_gyfcat"]
Collection4 = db[ user_name + "_Gallery_Links".lower()]
Collection5 = db[ user_name + "_imgur_album".lower()]
Collection6 = db[ user_name + "_raw".lower()]

mycursor = mydb.cursor()
sql1 = "DROP TABLE " + str(user_name)  + "_raw"
sql2 = "DROP TABLE " + str(user_name)  + "_pics"
sql3 = "DROP TABLE " + str(user_name)  + "_vid"
sql4 = "DROP TABLE " + str(user_name)  + "_gallery_links"
sql5 = "DROP TABLE " + str(user_name)  + "_gyfcat"
sql6 = "DROP TABLE " + str(user_name)  + "_imgur_album"

mycursor.execute(sql1)
mycursor.execute(sql2)
mycursor.execute(sql3)
mycursor.execute(sql4)
mycursor.execute(sql5)
mycursor.execute(sql6)

Collection1.drop()
Collection2.drop()
Collection3.drop()
Collection4.drop()
Collection5.drop()
Collection6.drop()

print("deleted tables from database ")