
unedited_redgif = open('txtxt.txt', 'r')
edited_redgif = open('imgur_album.txt','w+')

for line in unedited_redgif:
    if "imgur.com/a/" in line:
        print(line)
        edited_redgif.write(line)


unedited_redgif.close()
edited_redgif.close()
# -------------------------------------------------------------
#  to delete some words 

f = open('imgur_album.txt','r')
a = ['http://imgur.com/a/']
lst = []
for line in f:
    for word in a:
        if word in line:
            line = line.replace(word,'')
    lst.append(line)
f.close()
f = open('imgur_album.txt','w')
for line in lst:
    f.write(line)
    print(line)
f.close()

f = open('imgur_album.txt','r')
a = ['https://imgur.com/a/']
lst = []
for line in f:
    for word in a:
        if word in line:
            line = line.replace(word,'')
    lst.append(line)
f.close()
f = open('imgur_album.txt','w')
for line in lst:
    f.write(line)
    print(line)

f.close()


