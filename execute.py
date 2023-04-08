import os
import py_compile
import sys
import shutil
from colorama import Fore, Back, Style


# to take userInput for the /u/
input_var = input("Enter Username: ")
print ("you entered " + input_var) 

with open('sub_list.csv','w+') as file:
    file.write(input_var)
# --------------------------------------------------

if os.path.exists('temp_data'):
    shutil.rmtree('temp_data')
if os.path.exists('data'):
    shutil.rmtree('data')
    
os.system('python makedir.py')
# to clear some file data......
f = open('gyfcat_test.json', 'r+')
f.truncate(0)
f = open('gyfcat.txt', 'r+')
f.truncate(0)
f = open('temp_gyfcat.txt', 'r+')
f.truncate(0)
f = open('temp_redgif.txt', 'r+')
f.truncate(0)


os.system('python temp_final.py')
os.system('python onlyredgif.py')
os.system('python get_imgur_a_words.py')
os.system('python headers.py')
os.system('python imgur_headers.py')
os.system('python gyfcat.py')
os.system('python del_redgif.py')
os.system('python del_gifv_txt.py')
os.system('python GalleryDownload.py')
os.system('python gallery.py')
os.system('python del_gallerylinks.py')
os.system('python del_gycatlines.py')
os.system('python del_gifv_txt.py')
# os.system('python del_imgur_links.py')
# os.system('python upload_raw_data.py')
# os.system('python transfer_data.py')
# os.system('python jsonmaker.py')
# os.system('python cpy-temp_data.py')
# os.system('python transfer_to_mongo.py')
# os.system('python create_mysql_table.py')
# os.system('python push_data_mysql.py')
# os.system('python donwloadimages.py')
os.system('python beep.py')

print(Back.GREEN + 'HOGYA, TATA, BYEBYE')
print(Style.RESET_ALL)

my_file = "test.json"
base = os.path.splitext(my_file)[0]
# os.rename(my_file, base + '.txt')