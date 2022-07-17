list=['KFr0srv', 'GYUG00f', 'Ks8l87Q', 'G6Vp3Fp.gifv', '']nly_imgur_album.txt", "r")
  
# reading the file
data = my_file.read()
  
# replacing end splitting the text 
# when newline ('\n') is seen.
data_into_list = data.split("\n")
print(data_into_list)

file1 = open("imgur_headers.py","a") 

file1.close() 
# ------
line = 'list='
with open('imgur_headers.py', 'r+') as file: 
    file_data = file.read() 
    file.seek(0, 0) 
    file.write(str(line))
    file.write(str(data_into_list)) 



# print(word)
my_file.close()

# to find total words in only_imgur_album.txt
with open(r"only_imgur_album.txt", 'r') as fp:
    total_words = len(fp.readlines())
    print('Total Number of lines:', total_words)

# -------------------------------------------------------------------------
from asyncore import write
from imgurpython import ImgurClient

client_id = 'c855a613dd67e88'
client_secret = '38096eb1a62106569e51d648dc29ffd53ab6d582'

client = ImgurClient(client_id, client_secret)

print(total_words)
for x in range(total_words):
    # Example request
    items = client.get_album_images(list[x])
    for item in items:
        linkss = item.link
        print(linkss)
        # write the links in imgur_album_links.txt
        file = open('imgur_album_links.txt','a')
        file.write(str(linkss+'\n'))
        file.close()

# delte the list=[] in first line 

with open('imgur_headers.py', 'r') as fin:
    data = fin.read().splitlines(True)
with open('imgur_headers.py', 'w') as fout:
    fout.writelines(data[1:])

# --------------------------------------------------------------------------------------------------------------------