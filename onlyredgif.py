with open('txtxt.txt', 'r') as unedited_redgif:
    with open('redgif.txt','w') as edited_redgif:
        for line in unedited_redgif:
            if "redgif" in line:
                edited_redgif.write(line)

with open('redgif.txt', 'r') as f:
    lst = []
    for line in f:
        line = line.replace('https://redgifs.com/watch/', '')
        line = line.replace('https://www.redgifs.com/watch/', '')
        line = line.replace('http://redgifs.com/watch/', '')
        line = line.replace('http://www.redgifs.com/watch/', '')
        line = line.replace('https://v3.redgifs.com/watch/', '')
        line = line.replace('http://v3.redgifs.com/watch/', '')
        lst.append(line)

with open('redgif.txt', 'w') as f:
    for line in lst:
        f.write(line)
        print(line)
