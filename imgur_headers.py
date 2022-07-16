
from imgurpython import ImgurClient
import requests
client_id = 'c855a613dd67e88'
client_secret = '38096eb1a62106569e51d648dc29ffd53ab6d582'

client = ImgurClient(client_id, client_secret)

# # Example request
# items = client.get_album_images('X5Mnr')
# for item in items: 
#     print(item.link)

with open('imgur_album.txt','r') as word:
    all_words = word.readlines()
    print(all_words)