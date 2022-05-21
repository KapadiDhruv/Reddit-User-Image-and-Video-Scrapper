import os
import py_compile
import sys
import shutil
from colorama import Fore, Back, Style

shutil.rmtree('temp_data')
shutil.rmtree('data')

  
# first delete the file if you are performing again in order to delete the redundant data in redgif.txt
# os.remove("txt.txt")
# os.remove("txtxt.txt")
# os.remove("json.json")
# os.remove("test.json")
# os.remove("redgif.txt")
# os.remove('onlygallery.txt')
# os.remove('finalgallery.txt')
f = open('gyfcat_test.json', 'r+')
f.truncate(0)

os.system('python temp_final.py')
os.system('python onlyredgif.py')
os.system('python headers.py')
os.system('python gyfcat.py')
os.system('python del_redgif.py')
os.system('python del_gifv_txt.py')
os.system('python GalleryDownload.py')
os.system('python gallery.py')
os.system('python del_gallerylinks.py')
os.system('python del_gycatlines.py')
os.system('python del_gifv_txt.py')
os.system('python transfer_data.py')
os.system('python jsonmaker.py')
os.system('python jstgallery.py')
os.system('python cpy-temp_data.py')

print(Back.GREEN + 'HOGYA, TATA, BYEBYE')
print(Style.RESET_ALL)

my_file = "test.json"
base = os.path.splitext(my_file)[0]
# os.rename(my_file, base + '.txt')