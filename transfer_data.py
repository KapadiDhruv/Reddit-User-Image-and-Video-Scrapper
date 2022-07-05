import shutil
import os

# to create data folder if not existent
folder_path = 'data'
isExist = os.path.exists(folder_path) 

if(isExist != True):
    os.mkdir(folder_path)


# deleting the below lines in txt file and transfering to data/pics.txt
bad_words = ['watch','/r/', 'gallery']

with open('txt.txt','r') as oldfile, open('pics.txt', 'w+') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in bad_words):
            newfile.write(line)

# For images : 

original_1 = r'pics.txt'
target = r'data/pics.txt'

answer1 = os.stat("pics.txt").st_size == 0

if(answer1 != True):
    shutil.copyfile(original_1, target)

# For vid : 

original = r'test.json'
target = r'data/vid.txt'

answer1 = os.stat("test.json").st_size == 0

if(answer1 != True):
    shutil.copyfile(original, target)

# for gyfcat
original = r'gyfcat_test.json'
target = r'data/gyfcat.txt'

answer2 = os.stat("gyfcat_test.json").st_size == 0

if(answer2 != True):
    shutil.copyfile(original, target)


#  For Gallery : 

original = r'Gallery_Links.txt'
target = r'data/Gallery_Links.txt'

answer3 = os.stat("Gallery_Links.txt").st_size == 0

if(answer3 != True):
    shutil.copyfile(original, target)

# ------------------------------------------------------------------------------------------------------

# # To transfer files in the HDD 
# # Directory

# original = r'sub_list.csv'


# with open(original,'r') as firstfile: 
#     for line in firstfile:
#         directory = ('to do -' + line)
  
# # Parent Directory path
# parent_dir = "D:\Games\download\AA_here"
  
# # Path

# path = os.path.join( parent_dir, directory)
  
# # Create the directory
# # 'GeeksForGeeks' in
# # '/home / User / Documents'
# os.mkdir(path)
# os.mkdir(path + '\json_data')
# print("Directory '% s' created" % directory)


# # To move all the files from data to HDD

# source_dir = 'C:\pyth\data'
# target_dir = path
    
# file_names = os.listdir(source_dir)
    
# for file_name in file_names:
#     shutil.copy(os.path.join(source_dir, file_name), target_dir)


# # truncating the gyfcat_test.json file
# f = open("gyfcat_test.json", "a")
# f.truncate()
# f.close()

# # to delte the data folder
# # os.rmdir(folder_path)