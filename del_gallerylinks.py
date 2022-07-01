# delete galelery links from txt.txt file 

with open("Gallery_Links.txt",'r') as file:
    lines = file.readlines()

with open("Gallery_Links.txt",'w') as file:
    for line in lines:
        # find() returns -1 if no match is found
        if line.find("gallery") != -1:
            pass
        else:
            file.write(line)
