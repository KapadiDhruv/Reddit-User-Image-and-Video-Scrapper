# import os
# import fileinput
# import shutil
# from os.path import exists


# folder_path = 'temp_data'
# isExist = os.path.exists(folder_path) 

# if(isExist != True):
#     os.mkdir(folder_path)

# # for pics
# original_1 = r'data/pics.txt'
# target = r'temp_data/pics.txt'



# answer1 = os.stat("data/pics.txt").st_size == 0

# if(answer1 != True):
#     shutil.copyfile(original_1, target)
#     file_path = "data/pics.txt"

#     with open(file_path,"r+") as file:
#         lines = file.readlines()
#         file.seek(0)
#         # file.write('{'+ '\n')
#         file.write('['+ '\n')
#         for line in enumerate(lines):
#             to_write_string = str('{"url' + '"' +': ' + '"' +line)
#             file.write(to_write_string)
            
        


#     file_name = file_path
#     string_to_add = '"},'

#     with open(file_name, 'r') as f:
#         file_lines = [''.join([x.strip(), string_to_add, '\n']) for x in f.readlines()]

#     with open(file_name, 'w+') as f:
#         f.writelines(file_lines) 



#     with open('data/pics.txt', 'r') as f:
#         lines = f.read().splitlines()
#         last_line = lines[-1]
#         name = last_line.rstrip(last_line[-1])
#         # print(name)


#     #   to replace the last line ','
#         foo = name + ','
#         bar = name
        
#         file = open("data/pics.txt", "r")
#         replacement = ""
#         # using the for loop
#         for line in file:
#             line = line.strip()
#             changes = line.replace(foo,bar)
#             replacement = replacement + changes + "\n"

#         file.close()
#         # opening the file in write mode
#         fout = open("data/pics.txt", "w")
#         fout.write(replacement)
#         fout.write('}')
#         fout.close()


#     # to replace {",
#     with open('data/pics.txt', 'r') as f:
#         liness = f.read().splitlines()
#         last_linee = liness[0]
#         namee = last_linee.rstrip(last_linee[0])
#         print(namee)


#     #   to replace the last line ','
#         fooo = namee 
#         barr = '{'
        
#         file = open("data/pics.txt", "r")
#         replacementt = ""
#         # using the for loop
#         for line in file:
#             line = line.strip()
#             changess = line.replace(fooo,barr)
#             replacementt = replacementt + changess + "\n"

#         file.close()
#         # opening the file in write mode
#         fout = open("data/pics.txt", "w")
#         fout.write(replacementt)
#         fout.close()
#     # done till making json data----------------------------------------------------------------------------

#     shutil.copy("data/pics.txt", "temp_data/pics.txt")
#     os.rename("temp_data/pics.txt", "temp_data/pics.json")



from os.path import exists

import os 
import csv 
import json
import shutil 

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
          


# for pics
data_pics = exists('data/pics.txt')
if(data_pics == True):

    line = 'url'
    with open('data/pics.txt', 'r+') as file: 
        file_data = file.read() 
        file.seek(0, 0) 
        file.write(line + '\n' + file_data) 


    my_file = "data/pics.txt"
    base = os.path.splitext(my_file)[0]
    os.rename(my_file, base + '.csv')

# to convert the file from csv to json
    csvFilePath = r'data/pics.csv'
    jsonFilePath = r'data/pics.json'

    csv_to_json(csvFilePath, jsonFilePath)

else:
    print('no pics file found')
# *****************************************************************

# for videos
data_vid = exists('data/vid.txt')

if(data_vid == True):

    line = 'url'
    with open('data/vid.txt', 'r+') as file: 
        file_data = file.read() 
        file.seek(0, 0) 
        file.write(line + '\n' + file_data) 


    my_file = "data/vid.txt"
    base = os.path.splitext(my_file)[0]
    os.rename(my_file, base + '.csv')

# to convert the file from csv to json
    csvFilePath = r'data/vid.csv'
    jsonFilePath = r'data/vid.json'

    csv_to_json(csvFilePath, jsonFilePath)
else:
    print('no vid file found')

# *****************************************************************
# for gyfcat file
data_gyfcat = exists('data/gyfcat_test.txt')

if(data_gyfcat == True):

    line = 'url'
    with open('data/gyfcat_test.txt', 'r+') as file: 
        file_data = file.read() 
        file.seek(0, 0) 
        file.write(line + '\n' + file_data) 


    my_file = "data/gyfcat_test.txt"
    base = os.path.splitext(my_file)[0]
    os.rename(my_file, base + '.csv')
# to convert the file from csv to json
    csvFilePath = r'data/gyfcat_test.csv'
    jsonFilePath = r'data/gyfcat_test.json'

    csv_to_json(csvFilePath, jsonFilePath)
else:
    print('no gyfcat file found')

# *****************************************************************
# for gallery file
data_gallery = exists('data/Gallery_Links.txt')
if(data_gallery == True):

    line = 'url'
    with open('data/Gallery_Links.txt', 'r+') as file: 
        file_data = file.read() 
        file.seek(0, 0) 
        file.write(line + '\n' + file_data) 


    my_file = "data/Gallery_Links.txt"
    base = os.path.splitext(my_file)[0]
    os.rename(my_file, base + '.csv')

# to convert the file from csv to json
    csvFilePath = r'data/Gallery_Links.csv'
    jsonFilePath = r'data/Gallery_Links.json'

    csv_to_json(csvFilePath, jsonFilePath)
else:
    print('no  gallery file found')
# *****************************************************************
# for imgur_album
data_imgur_album = exists('data/imgur_album.txt')
if(data_imgur_album == True):

    line = 'url'
    with open('data/imgur_album.txt', 'r+') as file: 
        file_data = file.read() 
        file.seek(0, 0) 
        file.write(line + '\n' + file_data) 


    my_file = "data/imgur_album.txt"
    base = os.path.splitext(my_file)[0]
    os.rename(my_file, base + '.csv')

# to convert the file from csv to json
    csvFilePath = r'data/imgur_album.csv'
    jsonFilePath = r'data/imgur_album.json'

    csv_to_json(csvFilePath, jsonFilePath)
else:
    print('no imgur_album file found')

    

