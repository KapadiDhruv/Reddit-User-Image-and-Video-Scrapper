import json
import requests

with open('txtxt.txt') as input_data:
    gyfcat_urls = []
    for line in input_data:
        if "gfycat" in line:
            gyfcat_urls.append(line.strip())

gyfcat_urls = list(set(gyfcat_urls))  # remove duplicates

with open('gyfcat.txt', 'w') as outfile:
    for url in gyfcat_urls:
        outfile.write(url.replace('https://gfycat.com/', '') + '\n')

search_text = 'https://api.gfycat.com/v1/gfycats/'
replace_text = ''

with open('gyfcat.txt') as infile, open('gyfcat_test.json', 'w') as outfile:
    for line in infile:
        url = search_text + line.strip()
        response = requests.get(url)
        data = response.json()
        thumb_url = data.get('thumb100PosterUrl')
        if thumb_url:
            outfile.write(thumb_url + '\n')

search_text = 'https://thumbs.gfycat.com/'
replace_text1 = 'https://giant.gfycat.com/'
replace_text2 = '.mp4'

with open('gyfcat_test.json') as infile, open('gyfcat_links.txt', 'w') as outfile:
    for line in infile:
        url = line.strip().replace(search_text, replace_text1).replace('-mobile', '')
        url = url[:url.rindex('-')] + replace_text2
        outfile.write(url + '\n')
