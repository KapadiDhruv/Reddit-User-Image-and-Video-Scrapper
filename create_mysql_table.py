from telnetlib import GA
import mysql.connector

f_final = open("sub_list.csv", "r")
for line in f_final:
    user_name = line.strip()
    pics_qry =  f"""CREATE TABLE `reddit`.`{user_name + '_pics'}` (`id` INT NOT NULL AUTO_INCREMENT,`url` VARCHAR(45) NULL,PRIMARY KEY (`id`));"""
    print(pics_qry)       
    vid_qry =  f"""CREATE TABLE `reddit`.`{user_name + '_vid'}` (`id` INT NOT NULL AUTO_INCREMENT,`url` VARCHAR(45) NULL,PRIMARY KEY (`id`));"""
    print(vid_qry)       
    Gallery_Links_qry =  f"""CREATE TABLE `reddit`.`{user_name + '_Gallery_Links'}` (`id` INT NOT NULL AUTO_INCREMENT,`url` VARCHAR(45) NULL,PRIMARY KEY (`id`));"""
    print(Gallery_Links_qry)       
    Gyfcat_qry =  f"""CREATE TABLE `reddit`.`{user_name +'_Gyfcat'}` (`id` INT NOT NULL AUTO_INCREMENT,`url` VARCHAR(45) NULL,PRIMARY KEY (`id`));"""
    print(Gyfcat_qry)       
    imgur_qry =  f"""CREATE TABLE `reddit`.`{user_name +'_imgur_album'}` (`id` INT NOT NULL AUTO_INCREMENT,`url` VARCHAR(45) NULL,PRIMARY KEY (`id`));"""
    print(imgur_qry)       

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
    user_name_imgur         = imgur_qry

    
    # table created
    cursorObject.execute(user_name_pics) 
    cursorObject.execute(user_name_vid) 
    cursorObject.execute(user_name_Gallery_Links) 
    cursorObject.execute(user_name_Gyfcat) 
    cursorObject.execute(user_name_imgur) 
    
    # disconnecting from server
    dataBase.close()



