with open('txtxt.txt', 'r') as unedited_redgif, open('only_imgur_album.txt','w+') as edited_redgif:
    for line in unedited_redgif:
        if "imgur.com/a/" in line:
            print(line)
            edited_redgif.write(line)

words_to_replace = ['http://imgur.com/a/', 'https://imgur.com/a/', 'https://m.imgur.com/a/', 'http://m.imgur.com/a/']

with open('only_imgur_album.txt','r') as f:
    lst = []
    for line in f:
        for word in words_to_replace:
            if word in line:
                line = line.replace(word,'')
        lst.append(line)

with open('only_imgur_album.txt','w') as f:
    for line in lst:
        f.write(line)
        print(line)
