import sys, json, os
import traceback
import requests, time, shutil
import wget
import hashlib


  
# importing time module
import time


def url_file(redgifs_url, filename):

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
            video_url = ''
            if 'gif' in rawData and 'urls' in rawData['gif'] and 'hd' in rawData['gif']['urls']:
                video_url = rawData['gif']['urls']['hd']
                with sess.get(video_url, stream=True) as r:
                    with open(filename, 'wb') as f:
                        shutil.copyfileobj(r.raw, f)
                    video_hash = hashlib.sha256(open(filename, 'rb').read()).hexdigest()
                    return {'filename': filename, 'sha256': video_hash}

            elif 'gfyItem' in rawData and 'content_urls' in rawData['gfyItem'] and 'mp4' in rawData['gfyItem']['content_urls']:
                video_url = rawData['gfyItem']['content_urls']['mp4']['url']
                with sess.get(video_url, stream=True) as r:
                    with open(filename, 'wb') as f:
                        shutil.copyfileobj(r.raw, f)
                    video_hash = hashlib.sha256(open(filename, 'rb').read()).hexdigest()
                    return {'filename': filename, 'sha256': video_hash}
            else : 
                print("redgifs_url not present!")

    except Exception:
        # traceback.print_exc()
        return



f_final = open("sub_list.csv", "r")

for line in f_final:
    user = line.strip()

file = open(f'{user}//onlyredgif_{user}.txt',"r+")

# folder_name = user + '_vid'
folder_name = f'{user}\\videos_{user}'
if os.path.exists(folder_name):
    shutil.rmtree(folder_name)
os.mkdir(folder_name)

os.chdir(os.path.join(os.getcwd(), f'{folder_name}'))
video_info = {}
for line in file:
    sub = line.strip()
    print(sub)
    video_data = url_file(f"https://www.redgifs.com/watch/{sub}", f"{sub}.mp4")
    if video_data:
        video_info[sub] = video_data

with open('video_info.json', 'w') as f:
    json.dump(video_info, f)

folder_path = os.getcwd()

for filename in os.listdir(folder_path):
    filepath = os.path.join(folder_path, filename)
    if os.path.isfile(filepath) and os.path.getsize(filepath) == 0:
        print(f"File with size 0 found: {filename}")
        video_data = url_file(f"https://www.redgifs.com/watch/{filename[:-4]}", filepath)
        if video_data:
            with open('video_info.json', 'r') as f:
                video_info = json.load(f)
            video_info[filename[:-4]] = video_data
            with open('video_info.json', 'w') as f:
                json.dump(video_info, f)


# check the hash key and delete duplicate

with open('video_info.json', 'r') as f:
    video_info = json.load(f)

seen_hashes = set()
for sub, data in video_info.items():
    sha = data['sha256']
    if sha in seen_hashes:
        os.remove(data['filename'])
        print(f"Deleted file with duplicate SHA-256 hash: {data['filename']}")
    else:
        seen_hashes.add(sha)

# Update the video_info.json file to remove entries for deleted files
for sub, data in list(video_info.items()):
    if not os.path.exists(data['filename']):
        del video_info[sub]

with open('video_info.json', 'w') as f:
    json.dump(video_info, f,indent=4)
