    
from asyncore import write
from imgurpython import ImgurClient

client_id = 'c855a613dd67e88'
client_secret = '38096eb1a62106569e51d648dc29ffd53ab6d582'
with open("only_imgur_album.txt", "r") as file:
    total_words = len(file.readlines())
    # print(total_words)

    client = ImgurClient(client_id, client_secret)

    with open("only_imgur_album.txt", "r") as text_file:
        data = text_file.readlines()
        for x in range(total_words):
            temp = data[x].strip()
            # real_data = f"'{temp}'"
            # print(temp)
            # print(real_data)
            # items = client.get_album_images(list[x])
            items = client.get_album_images('%s' %temp)
            # items = client.get_album_images('%s' %real_data)
            for item in items:
                linkss = item.link
                print(linkss)

                # write the links in imgur_album_links.txt
                file = open('imgur_album_links.txt','a')
                file.write(str(linkss+'\n'))
                file.close()