from imgurpython import ImgurClient

client_id = 'c855a613dd67e88'
client_secret = '38096eb1a62106569e51d648dc29ffd53ab6d582'

with open("only_imgur_album.txt", "r") as file:
    data = file.readlines()
    total_words = len(data)

    client = ImgurClient(client_id, client_secret)

    with open("imgur_album_links.txt", "w") as output_file:
        for idx, link in enumerate(data):
            link = link.strip()
            items = client.get_album_images(link)
            for item in items:
                output_file.write(f"{item.link}\n")
