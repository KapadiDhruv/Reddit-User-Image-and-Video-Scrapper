import os
import re


file1 = open('txtxt.txt','r')
file2 = open('txt.txt','w')
for line in file1.readlines():
  
    x = re.findall("^https://gfycat.com" , line)
    if not x:
        
        print(line)
        file2.write(line)
    

file1.close()
file2.close()

