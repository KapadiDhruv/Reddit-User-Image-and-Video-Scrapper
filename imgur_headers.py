# from imgurpython import ImgurClient

# client_id = 'c855a613dd67e88'
# client_secret = '38096eb1a62106569e51d648dc29ffd53ab6d582'

# with open("only_imgur_album.txt", "r") as file:
#     data = file.readlines()
#     total_words = len(data)

#     client = ImgurClient(client_id, client_secret)

#     with open("imgur_album_links.txt", "w") as output_file:
#         for idx, link in enumerate(data):
#             link = link.strip()
#             items = client.get_album_images(link)
#             for item in items:
#                 output_file.write(f"{item.link}\n")
from imgurpython import ImgurClient
import os

client_id = 'c855a613dd67e88'
client_secret = '38096eb1a62106569e51d648dc29ffd53ab6d582'

with open('sub_list.csv', 'r') as f_final:
    for line in f_final:
        user = line.strip()
        album_file = os.path.join(user, f"only_imgur_album_{user}.txt")
        if os.path.exists(album_file):
            with open(album_file, 'r') as file:
                data = file.readlines()
                total_words = len(data)

                client = ImgurClient(client_id, client_secret)

                with open(f"{user}/imgur_album_links_{user}.txt", "w") as output_file:
                    for idx, link in enumerate(data):
                        link = link.strip()
                        items = client.get_album_images(link)
                        for item in items:
                            output_file.write(f"{item.link}\n")
        else:
            print(f"File {album_file} does not exist for user {user}. Skipping...")
