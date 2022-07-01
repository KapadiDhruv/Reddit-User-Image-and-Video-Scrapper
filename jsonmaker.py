import os
import fileinput
import shutil
from os.path import exists


folder_path = 'temp_data'
isExist = os.path.exists(folder_path) 

if(isExist != True):
    os.mkdir(folder_path)

# for pics
original_1 = r'data/pics.txt'
target = r'temp_data/pics.txt'



answer1 = os.stat("data/pics.txt").st_size == 0

if(answer1 != True):
    shutil.copyfile(original_1, target)
    file_path = "data/pics.txt"

    with open(file_path,"r+") as file:
        lines = file.readlines()
        file.seek(0)
        file.write('{'+ '\n')
        for index,line in enumerate(lines):
            to_write_string = str('"name' + str(index) + '"' +': ' + '"' +line)
            file.write(to_write_string)
            
        


    file_name = file_path
    string_to_add = '",'

    with open(file_name, 'r') as f:
        file_lines = [''.join([x.strip(), string_to_add, '\n']) for x in f.readlines()]

    with open(file_name, 'w+') as f:
        f.writelines(file_lines) 



    with open('data/pics.txt', 'r') as f:
        lines = f.read().splitlines()
        last_line = lines[-1]
        name = last_line.rstrip(last_line[-1])
        # print(name)


    #   to replace the last line ','
        foo = name + ','
        bar = name
        
        file = open("data/pics.txt", "r")
        replacement = ""
        # using the for loop
        for line in file:
            line = line.strip()
            changes = line.replace(foo,bar)
            replacement = replacement + changes + "\n"

        file.close()
        # opening the file in write mode
        fout = open("data/pics.txt", "w")
        fout.write(replacement)
        fout.write('}')
        fout.close()


    # to replace {",
    with open('data/pics.txt', 'r') as f:
        liness = f.read().splitlines()
        last_linee = liness[0]
        namee = last_linee.rstrip(last_linee[0])
        print(namee)


    #   to replace the last line ','
        fooo = namee 
        barr = '{'
        
        file = open("data/pics.txt", "r")
        replacementt = ""
        # using the for loop
        for line in file:
            line = line.strip()
            changess = line.replace(fooo,barr)
            replacementt = replacementt + changess + "\n"

        file.close()
        # opening the file in write mode
        fout = open("data/pics.txt", "w")
        fout.write(replacementt)
        fout.close()
    # done till making json data----------------------------------------------------------------------------

    shutil.copy("data/pics.txt", "temp_data/pics.txt")
    os.rename("temp_data/pics.txt", "temp_data/pics.json")


# for vid
original_1 = r'data/vid.txt'
target = r'temp_data/vid.txt'

answer1 = os.stat("data/vid.txt").st_size == 0

if(answer1 != True):
    shutil.copyfile(original_1, target)
    file_path = "data/vid.txt"

    with open(file_path,"r+") as file:
        lines = file.readlines()
        file.seek(0)
        file.write('{'+ '\n')
        for index,line in enumerate(lines):
            to_write_string = str('"name' + str(index) + '"' +': ' + '"' +line)
            file.write(to_write_string)
            
        


    file_name = file_path
    string_to_add = '",'

    with open(file_name, 'r') as f:
        file_lines = [''.join([x.strip(), string_to_add, '\n']) for x in f.readlines()]

    with open(file_name, 'w+') as f:
        f.writelines(file_lines) 



    with open('data/vid.txt', 'r') as f:
        lines = f.read().splitlines()
        last_line = lines[-1]
        name = last_line.rstrip(last_line[-1])
        # print(name)


    #   to replace the last line ','
        foo = name + ','
        bar = name
        
        file = open("data/vid.txt", "r")
        replacement = ""
        # using the for loop
        for line in file:
            line = line.strip()
            changes = line.replace(foo,bar)
            replacement = replacement + changes + "\n"

        file.close()
        # opening the file in write mode
        fout = open("data/vid.txt", "w")
        fout.write(replacement)
        fout.write('}')
        fout.close()


    # to replace {",
    with open('data/vid.txt', 'r') as f:
        liness = f.read().splitlines()
        last_linee = liness[0]
        namee = last_linee.rstrip(last_linee[0])
        # print(namee)


    #   to replace the last line ','
        fooo = namee 
        barr = '{'
        
        file = open("data/vid.txt", "r")
        replacementt = ""
        # using the for loop
        for line in file:
            line = line.strip()
            changess = line.replace(fooo,barr)
            replacementt = replacementt + changess + "\n"

        file.close()
        # opening the file in write mode
        fout = open("data/vid.txt", "w")
        fout.write(replacementt)
        fout.close()
    # done till making json data----------------------------------------------------------------------------

    shutil.copy("data/vid.txt", "temp_data/vid.txt")
    os.rename("temp_data/vid.txt", "temp_data/vid.json")


# for Gallery_Links
original_1 = r'data/Gallery_Links.txt'
target = r'temp_data/Gallery_Links.txt'



answer1 = os.stat("data/Gallery_Links.txt").st_size == 0

if(answer1 != True):
    shutil.copyfile(original_1, target)
    file_path = "data/Gallery_Links.txt"

    with open(file_path,"r+") as file:
        lines = file.readlines()
        file.seek(0)
        file.write('{'+ '\n')
        for index,line in enumerate(lines):
            to_write_string = str('"name' + str(index) + '"' +': ' + '"' +line)
            file.write(to_write_string)
            
        


    file_name = file_path
    string_to_add = '",'

    with open(file_name, 'r') as f:
        file_lines = [''.join([x.strip(), string_to_add, '\n']) for x in f.readlines()]

    with open(file_name, 'w+') as f:
        f.writelines(file_lines) 



    with open('data/Gallery_Links.txt', 'r') as f:
        lines = f.read().splitlines()
        last_line = lines[-1]
        name = last_line.rstrip(last_line[-1])
        # print(name)


    #   to replace the last line ','
        foo = name + ','
        bar = name
        
        file = open("data/Gallery_Links.txt", "r")
        replacement = ""
        # using the for loop
        for line in file:
            line = line.strip()
            changes = line.replace(foo,bar)
            replacement = replacement + changes + "\n"

        file.close()
        # opening the file in write mode
        fout = open("data/Gallery_Links.txt", "w")
        fout.write(replacement)
        fout.write('}')
        fout.close()


    # to replace {",
    with open('data/Gallery_Links.txt', 'r') as f:
        liness = f.read().splitlines()
        last_linee = liness[0]
        namee = last_linee.rstrip(last_linee[0])
        # print(namee)


    #   to replace the last line ','
        fooo = namee 
        barr = '{'
        
        file = open("data/Gallery_Links.txt", "r")
        replacementt = ""
        # using the for loop
        for line in file:
            line = line.strip()
            changess = line.replace(fooo,barr)
            replacementt = replacementt + changess + "\n"

        file.close()
        # opening the file in write mode
        fout = open("data/Gallery_Links.txt", "w")
        fout.write(replacementt)
        fout.close()
    # done till making json data----------------------------------------------------------------------------

    shutil.copy("data/Gallery_Links.txt", "temp_data/Gallery_Links.txt")
    os.rename("temp_data/Gallery_Links.txt", "temp_data/Gallery_Links.json")




#  for gyfcat

original_1 = r'data/gyfcat_test.txt'
target = r'temp_data/gyfcat_test.txt'



answer1 = os.stat("data/gyfcat_test.txt").st_size == 0

if(answer1 != True):
    shutil.copyfile(original_1, target)
    file_path = "data/gyfcat_test.txt"

    with open(file_path,"r+") as file:
        lines = file.readlines()
        file.seek(0)
        file.write('{'+ '\n')
        for index,line in enumerate(lines):
            to_write_string = str('"name' + str(index) + '"' +': ' + '"' +line)
            file.write(to_write_string)
            
        


    file_name = file_path
    string_to_add = '",'

    with open(file_name, 'r') as f:
        file_lines = [''.join([x.strip(), string_to_add, '\n']) for x in f.readlines()]

    with open(file_name, 'w+') as f:
        f.writelines(file_lines) 



    with open('data/gyfcat_test.txt', 'r') as f:
        lines = f.read().splitlines()
        last_line = lines[-1]
        name = last_line.rstrip(last_line[-1])
        # print(name)


    #   to replace the last line ','
        foo = name + ','
        bar = name
        
        file = open("data/gyfcat_test.txt", "r")
        replacement = ""
        # using the for loop
        for line in file:
            line = line.strip()
            changes = line.replace(foo,bar)
            replacement = replacement + changes + "\n"

        file.close()
        # opening the file in write mode
        fout = open("data/gyfcat_test.txt", "w")
        fout.write(replacement)
        fout.write('}')
        fout.close()


    # to replace {",
    with open('data/gyfcat_test.txt', 'r') as f:
        liness = f.read().splitlines()
        last_linee = liness[0]
        namee = last_linee.rstrip(last_linee[0])
        # print(namee)


    #   to replace the last line ','
        fooo = namee 
        barr = '{'
        
        file = open("data/gyfcat_test.txt", "r")
        replacementt = ""
        # using the for loop
        for line in file:
            line = line.strip()
            changess = line.replace(fooo,barr)
            replacementt = replacementt + changess + "\n"

        file.close()
        # opening the file in write mode
        fout = open("data/gyfcat_test.txt", "w")
        fout.write(replacementt)
        fout.close()
    # done till making json data----------------------------------------------------------------------------

    shutil.copy("data/gyfcat_test.txt", "temp_data/gyfcat_test.txt")
    os.rename("temp_data/gyfcat_test.txt", "temp_data/gyfcat_test.json")






