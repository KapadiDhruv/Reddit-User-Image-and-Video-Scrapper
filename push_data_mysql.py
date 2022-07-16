# #  to pass the data_to_read to mysql 

from importlib.resources import path
import pandas as pd
import os
from sqlalchemy import create_engine, engine
from os.path import exists
from colorama import Fore, Back, Style



original = r'sub_list.csv'

with open(original,'r') as firstfile: 
    for user_name in firstfile:
        print(os.getcwd())

        #  pics
        if(exists(os.path.join(os.getcwd() + '/to do - ' + user_name + '/pics.json'))):
            engine = create_engine('mysql+pymysql://root:dhruv@localhost/reddit')
            pics = os.path.join(os.getcwd() + '/to do - ' + user_name + '/pics.json')

            df = pd.read_json(pics)
            table_name = (user_name + '_pics').lower()
            # database name always save in db in small letters
            df.to_sql(table_name,con=engine,if_exists='replace')

            print(Back.GREEN +'pics.json uploaded in mysql Database')
            print(Style.RESET_ALL)

        else:
            print(Back.RED + 'No pics.json file found to upload on Database')
            print(Style.RESET_ALL)
# ----------------------------------------------------------------------------------------------------
        #  vid
        if(exists(os.path.join(os.getcwd() + '/to do - ' + user_name + '/vid.json'))):
            engine = create_engine('mysql+pymysql://root:dhruv@localhost/reddit')
            vid = os.path.join(os.getcwd() + '/to do - ' + user_name + '/vid.json')
            df = pd.read_json(vid)
            table_name = (user_name + '_vid').lower()
            
            # database name always save in db in small letters
            df.to_sql(table_name,con=engine,if_exists='replace')

            print(Back.GREEN +'vid.json uploaded in mysql Database')
            print(Style.RESET_ALL)

        else:
            print(Back.RED + 'No vid.json file found to upload on Database')
            print(Style.RESET_ALL)
# ----------------------------------------------------------------------------------------------------
        #  Gallery_Links
        if(exists(os.path.join(os.getcwd() + '/to do - ' + user_name + '/Gallery_Links.json'))):
            engine = create_engine('mysql+pymysql://root:dhruv@localhost/reddit')
            Gallery_Links = os.path.join(os.getcwd() + '/to do - ' + user_name + '/Gallery_Links.json')
            df = pd.read_json(Gallery_Links)
            table_name = (user_name + '_Gallery_Links').lower()
            # database name always save in db in small letters
            df.to_sql(table_name,con=engine,if_exists='replace')

            print(Back.GREEN +'Gallery_Links.json uploaded in mysql Database')
            print(Style.RESET_ALL)

        else:
            print(Back.RED + 'No Gallery_Links.json file found to upload on Database')
            print(Style.RESET_ALL)

# ----------------------------------------------------------------------------------------------------
        #  Gyfcat
        if(exists(os.path.join(os.getcwd() + '/to do - ' + user_name + '/gyfcat_test.json'))):
            engine = create_engine('mysql+pymysql://root:dhruv@localhost/reddit')
            gyfcat_test = os.path.join(os.getcwd() + '/to do - ' + user_name + '/gyfcat_test.json')
            df = pd.read_json(Gallery_Links)
            table_name = (user_name + '_gyfcat').lower()
            # database name always save in db in small letters
            df.to_sql(table_name,con=engine,if_exists='replace')

            print(Back.GREEN +'gyfcat_test.json uploaded in mysql Database')
            print(Style.RESET_ALL)

        else:
            print(Back.RED + 'No gyfcat_test.json file found to upload on Database')
            print(Style.RESET_ALL)
