import os 

os.system("python final.py")

# To delete the "NONE" term
with open("txtxt.txt",'r') as file:
    lines = file.readlines()

with open("txtxt.txt",'w') as file:
    for line in lines:
        # find() returns -1 if no match is found
        if line.find("None") != -1:
            pass
        else:
            file.write(line)
