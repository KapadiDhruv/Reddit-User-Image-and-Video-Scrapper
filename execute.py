import os
import py_compile
import sys
import shutil

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
    
os.system('python3 makedir.py')
# to clear some file data......
f = open('gyfcat_test.json', 'r+')
f.truncate(0)
f = open('gyfcat.txt', 'r+')
f.truncate(0)
f = open('temp_gyfcat.txt', 'r+')
f.truncate(0)
f = open('temp_redgif.txt', 'r+')
f.truncate(0)


os.system('python3 temp_final.py')
os.system('python3 onlyredgif.py')
os.system('python3 get_imgur_a_words.py')
os.system('python3 headers.py')
os.system('python3 imgur_headers.py')
os.system('python3 gyfcat.py')
os.system('python3 del_redgif.py')
os.system('python3 del_gifv_txt.py')
os.system('python3 GalleryDownload.py')
os.system('python3 gallery.py')
os.system('python3 del_gallerylinks.py')
os.system('python3 del_gycatlines.py')
os.system('python3 del_gifv_txt.py')
os.system('python3 del_imgur_links.py')
# os.system('python3 upload_raw_data.py')
# os.system('python3 transfer_data.py')
# os.system('python3 jsonmaker.py')
# os.system('python3 cpy-temp_data.py')
# os.system('python3 create_mysql_table.py')
# os.system('python3 push_data_mysql.py')
os.system('python3 donwloadimages.py')
os.system('python3 downloadgalleryimages.py')
# os.system('python3 uploadtodrive.py')
# os.system('python3 transfer_to_mongo.py')
# os.system('python3 uploadtogcp.py')
# os.system('python3 beep.py')

my_file = "test.json"
base = os.path.splitext(my_file)[0]
# os.rename(my_file, base + '.txt')