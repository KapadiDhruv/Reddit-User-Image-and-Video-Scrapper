
from distutils import extension
import os 
import shutil
from os.path import exists
from pathlib import Path


# to make "temp_data" dest_path

dir_exists = exists('temp_data')
# print(dir_exists)
if (dir_exists == True):
    print('temp_data dest_path present....')
else:
    os.mkdir('temp_data')



src = str(os.getcwd() + '\\data')
dest = str(os.getcwd() + '\\temp_data')

src_files = os.listdir(src)

for files in src_files:
    if files.endswith('.json'):
        shutil.move(os.path.join(src,files), os.path.join(dest,files))



# #  to transfer to hdd
original = r'sub_list.csv'

with open(original,'r') as firstfile: 
    for line in firstfile:
        directory = ('to do - ' + line)
        os.mkdir(directory)
        src = str(os.getcwd() + '\\temp_data')
        print(src)
        dest = str(os.getcwd() + '\\' + directory )
        # dest1 = os.path.join('D:\Games\download\AA_here' + '\\' + directory )
        parent_dir = "D:\Games\download\AA_here"
        path = os.path.join( parent_dir, directory)
        os.mkdir(path)
        json_dest = path + '\json_data'
        os.mkdir(path + '\json_data')

       
        src_files = os.listdir(src)

        for files in src_files:
            if files.endswith('.json'):
                shutil.copy2(os.path.join(src,files), os.path.join(dest,files))
                shutil.copy2(os.path.join(src,files), os.path.join(json_dest,files))
# --------------------------------------------------------------------------------------------------------------------------

# to delte the url term in the csv files


# pics
if(exists('data/pics.csv')):
    with open('data/pics.csv', 'r') as fin:
        data = fin.read().splitlines(True)
    with open('data/pics.csv', 'w') as fout:
        fout.writelines(data[1:])
else:
    print('nothing to del...')


# vid
if(exists('data/vid.csv')):
    with open('data/vid.csv', 'r') as fin:
        data = fin.read().splitlines(True)
    with open('data/vid.csv', 'w') as fout:
        fout.writelines(data[1:])
else:
    print('nothing to del...')


# gyfcat
if(exists('data/gyfcat.csv')):
    with open('data/gyfcat.csv', 'r') as fin:
        data = fin.read().splitlines(True)
    with open('data/gyfcat.csv', 'w') as fout:
        fout.writelines(data[1:])
else:
    print('nothing to del...')



# gallery

if(exists('data/Gallery_Links.csv')):
    with open('data/Gallery_Links.csv', 'r') as fin:
        data = fin.read().splitlines(True)
    with open('data/Gallery_Links.csv', 'w') as fout:
        fout.writelines(data[1:])
else:
    print('nothing to del...')    


# ----------------------------------------------------------------------------------------------------------------------------
 # to transfer the "data" csv files to hdd
parent_dir = "D:\Games\download\AA_here"
with open(original,'r') as firstfile: 
    for line in firstfile:
        directory = ('to do - ' + line)

data_path = str(os.path.join(os.getcwd() + '\\data'))
dest_path = os.path.join( parent_dir, directory)

data_path_files = os.listdir(data_path)    

for csvfiles in data_path_files:
    if csvfiles.endswith('.csv'):
        shutil.copy2(os.path.join(data_path,csvfiles), os.path.join(dest_path,csvfiles))

for filename in os.listdir(dest_path):
    infilename = os.path.join(dest_path,filename)
    if not os.path.isfile(infilename): continue
    oldbase = os.path.splitext(filename)
    newname = infilename.replace('.csv', '.txt')
    output = os.rename(infilename, newname)

        