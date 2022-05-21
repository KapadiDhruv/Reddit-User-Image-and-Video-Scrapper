# To transfer files in the HDD 
# Directory

import os 
import shutil
from os.path import exists

original = r'sub_list.csv'


with open(original,'r') as firstfile: 
    for line in firstfile:
        directory = ('to do -' + line)
  
# Parent Directory path
parent_dir = r"D:\Games\download\AA_here"
  
# Path

path = os.path.join( parent_dir, (directory + '\json_data'))
  

# os.mkdir(path)
# os.mkdir(path + '\json_data')
print("Directory '% s' created" % directory)


# To move all the files from data to HDD

source_dir = r'temp_data'
target_dir = path
    
file_names = os.listdir(source_dir)
    
for file_name in file_names:
    shutil.copy(os.path.join(source_dir, file_name), target_dir)

file_exists = exists(path +"\Gallery_Links.txt")
if(file_exists == True):
    os.remove(path +"\Gallery_Links.txt")

