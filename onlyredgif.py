


unedited_redgif = open('txtxt.txt', 'r')
edited_redgif = open('redgif.txt','w')

for line in unedited_redgif:
    if "redgif" in line:
        print(line)
        edited_redgif.write(line)


unedited_redgif.close()
edited_redgif.close()
# -------------------------------------------------------------
#  to delete some words 

f = open('redgif.txt','r')
a = ['https://redgifs.com/watch/']
lst = []
for line in f:
    for word in a:
        if word in line:
            line = line.replace(word,'')
    lst.append(line)
f.close()
f = open('redgif.txt','w')
for line in lst:
    f.write(line)
f.close()

f = open('redgif.txt','r')
a = ['https://www.redgifs.com/watch/']
lst = []
for line in f:
    for word in a:
        if word in line:
            line = line.replace(word,'')
    lst.append(line)
f.close()
f = open('redgif.txt','w')
for line in lst:
    f.write(line)
f.close()