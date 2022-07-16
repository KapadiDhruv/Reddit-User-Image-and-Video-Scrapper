from telnetlib import GA
import mysql.connector

f_final = open("sub_list.csv", "r")
for line in f_final:
    user_name = line.strip()
    pics_qry =  f"""CREATE TABLE `reddit`.`{user_name + '_pics'}` (`id` INT NOT NULL AUTO_INCREMENT,`url` VARCHAR(45) NULL,PRIMARY KEY (`id`));"""
    vid_qry =  f"""CREATE TABLE `reddit`.`{user_name + '_vid'}` (`id` INT NOT NULL AUTO_INCREMENT,`url` VARCHAR(45) NULL,PRIMARY KEY (`id`));"""
    Gallery_Links_qry =  f"""CREATE TABLE `reddit`.`{user_name + '_Gallery_Links'}` (`id` INT NOT NULL AUTO_INCREMENT,`url` VARCHAR(45) NULL,PRIMARY KEY (`id`));"""
    Gyfcat_qry =  f"""CREATE TABLE `reddit`.`{user_name +'_Gyfcat'}` (`id` INT NOT NULL AUTO_INCREMENT,`url` VARCHAR(45) NULL,PRIMARY KEY (`id`));"""
    print(pics_qry)       

    # connecting to the database
    dataBase = mysql.connector.connect(
                        host = "localhost",
                        user = "root",
                        passwd = "dhruv",
                        database = "reddit" ) 
    
    # preparing a cursor object
    cursorObject = dataBase.cursor()
    
    # creating table 
    user_name_pics          = pics_qry
    user_name_vid           = vid_qry
    user_name_Gallery_Links = Gallery_Links_qry
    user_name_Gyfcat        = Gyfcat_qry

    
    # table created
    cursorObject.execute(user_name_pics) 
    cursorObject.execute(user_name_vid) 
    cursorObject.execute(user_name_Gallery_Links) 
    cursorObject.execute(user_name_Gyfcat) 
    
    # disconnecting from server
    dataBase.close()



