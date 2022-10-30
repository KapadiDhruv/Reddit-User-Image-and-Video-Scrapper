# from asyncore import write
# from textwrap import indent
# import requests
# import json
# import os
# import pandas as pd
# import requests
# import sys
# import string

# file = open('redgif.txt',"r+")
# for line in file:
#     sub = line.strip()
#     # print(sub)
#     url = "https://api.redgifs.com/v2/gifs/"
#     term = sub
#     # print(url + term)
#     r = requests.get(url + term)
#     print(r.json())
    # with open('json.json', 'w') as f:
    #     f.write(json.dumps(r.json(), indent = 1))

#     json_file = open('json.json', 'r')
#     edited_file = open('test.json','a')

#     for line in json_file:
#         if "hd" in line:
#             print(line)
#             edited_file.write(line)

#     json_file.close()
#     edited_file.close()
# print("-----------------------------------------------")

# search_text = '"hd": "'
# search_text1 = '",'
# replace_text = " "

# with open(r'test.json', 'r') as file:
#     data = file.read()
#     data = data.replace(search_text, replace_text)
#     data = data.replace(search_text1, replace_text)

# with open(r'test.json', 'w') as file:
#     file.write(data)
#     print("Text replaced")
        
    

# # word_1 = '"hd": "'
# # word_2 = '",'
# # f_file = "test.json"
# # delete_list = [word_1,word_2]
# # with open(f_file,"r+") as fin, open(f_file, "w+") as fout:
# #     for line in fin:
# #         for word in delete_list:
# #             line = line.replace(word, "")
# #         fout.write(line)
        
# # f_file.close()


# ````````````````````````````````````````````````````````````````````````````````
import sys, json, os
import traceback
import requests, time, shutil
import wget


def url_file(redgifs_url, filename):
    """
    It takes a RedGifs URL and a filename, and downloads the video to the filename
    
    :param redgifs_url: The URL of the RedGifs video you want to download
    :param filename: The name of the file to save the video as
    :return: The URL of the HD video.
    """
    sys.stdout.reconfigure(encoding='utf-8')
    API_URL_REDGIFS = 'https://api.redgifs.com/v1/gifs/'
    try:
        print("redgifs_url = {}".format(redgifs_url))

        #Get RedGifs video ID
        redgifs_ID = redgifs_url.split('/watch/', 1)
        redgifs_ID = redgifs_ID[1]
        print("redgifs_ID = {}".format(redgifs_ID))
        
        sess = requests.Session()
        
        request = sess.get(API_URL_REDGIFS + redgifs_ID)

        
        if request is None:
            return
        else:
            rawData = request.json()
            url = 'http://localhost:3000'
            myobj = {'data': rawData}

            x = requests.post(url, json = myobj)

            # print(x.json())
            with sess.get(x.json(), stream=True) as r:
                open(filename, 'wb').write(r.content)

            #     #Get HD video url
            # if rawData['gif']: 
            #     hd_video_url = rawData['gif']['urls']['hd']
            #     print("URL = {}".format(hd_video_url))
            #     # still to make the file of vid.json
            #     # with open('test.json', 'w') as f:
            #     #     f.write(hd_video_url)                    

                
            #     with sess.get(hd_video_url, stream=True) as r:
            #         with open(filename, 'wb') as f:
            #             for chunk in r.iter_content(chunk_size=8192): 
            #                 f.write(chunk)

            #     return hd_video_url
            
            # else:
            #     hd_video_url = rawData['gfyItem']['content_urls']['mp4']['url']
            #     print("URL = {}".format(hd_video_url))
            #     # still to make the file of vid.json
            #     with open('test.json', 'w') as f:
            #         f.write(hd_video_url)                    

                
            #     with sess.get(hd_video_url, stream=True) as r:
            #         with open(filename, 'wb') as f:
            #             for chunk in r.iter_content(chunk_size=8192): 
            #                 f.write(chunk)

            #     return hd_video_url


    except Exception:
        # traceback.print_exc()
        return

file = open('redgif.txt',"r+")
os.mkdir("vid")
os.chdir(os.path.join(os.getcwd() + "\\vid"))
for line in file:
    sub = line.strip()
    print(sub)
    url_file(f"https://www.redgifs.com/watch/{sub}", f"{sub}.mp4")
 


