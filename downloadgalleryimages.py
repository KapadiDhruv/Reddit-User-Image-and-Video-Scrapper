import os
import requests
import hashlib
import json
from os.path import exists
import time
from prettytable import PrettyTable
from PIL import Image, ImageDraw, ImageFont

start_time = time.time()

# Define font to use for the images
# font = ImageFont.truetype("arial.ttf", size=12)

with open("sub_list.csv", "r") as f_subreddits:
    for sub in f_subreddits:
        sub = sub.strip()
        username = sub

    pics_directory = f"{username}/gallery_pics_{username}"
    if not exists(pics_directory):
        os.makedirs(pics_directory, exist_ok=True)

    filename = f"{username}/gallery_pics_downloads.json"
    with open(f"{username}/cleaned_gallerylinks_{username}.txt", "r") as f:
        urls = f.read().splitlines()

    try:
        with open(filename, "r") as f:
            downloads = json.load(f)
    except FileNotFoundError:
        downloads = {}

    index = 1
    duplicates = 0
    total_download_time = 0
    for url in urls:
        response = requests.get(url)
        file_content = response.content
        file_hash = hashlib.sha256(file_content).hexdigest()
        filename = url.split("/")[-1]
        if file_hash in downloads.values():
            duplicates += 1
        else:
            start_download_time = time.time()
            file_name = f"{index}_{filename}"
            with open(f"{pics_directory}/{file_name}", "wb") as f:
                f.write(file_content)
            downloads[file_name] = {"hash": file_hash, "time": time.time() - start_download_time, "size": len(file_content)}
            total_download_time += downloads[file_name]["time"]
            index += 1

    total_download_time_str = f"{total_download_time:.2f} seconds" if total_download_time >= 1 else f"{total_download_time * 1000:.2f} ms"

    download_stats_table = PrettyTable(["Filename", "Time taken", "Size"])
    for download in downloads:
        file_name = download.split("_", 1)[1]
        time_taken = f"{downloads[download]['time']:.2f} seconds" if downloads[download]['time'] >= 1 else f"{downloads[download]['time'] * 1000:.2f} ms"
        size = f"{downloads[download]['size'] / 1024 / 1024:.2f} MB"
        download_stats_table.add_row([file_name, time_taken, size])

    duplicate_stats_table = PrettyTable(["Statistic", "Value"])
    duplicate_stats_table.add_row(["Number of duplicates detected", duplicates])

    time_stats_table = PrettyTable(["Statistic", "Value"])
    time_stats_table.add_row(["Number of files downloaded", index - 1])
    time_stats_table.add_row(["Total download time", total_download_time_str])

    # Create images of tables and save them in the directory where images are downloaded
    img1 = Image.new('RGB', (1200, 500), color=(255, 255, 255))
    d = ImageDraw.Draw(img1)
    d.text((10, 10), download_stats_table.get_string(), fill=(0, 0, 0))
    img1.save(f"{pics_directory}/downloads_table.png")

    img2 = Image.new('RGB', (500, 100), color = (255, 255, 255))
    d = ImageDraw.Draw(img2)
    d.text((10, 10), duplicate_stats_table.get_string(), fill=(0, 0, 0))
    img2.save(f"{pics_directory}/duplicates_table.png")

    img3 = Image.new('RGB', (500, 100), color = (255, 255, 255))
    d = ImageDraw.Draw(img3)
    d.text((10, 10), time_stats_table.get_string(), fill=(0, 0, 0))
    img3.save(f"{pics_directory}/time_stats_table.png")

    print(f"Downloaded {index-1} files with {duplicates} duplicates detected in {total_download_time_str}")
    print(f"Download statistics:\n{download_stats_table}")
    print(f"Duplicate statistics:\n{duplicate_stats_table}")
    print(f"Time statistics:\n{time_stats_table}")
    print(f"Total execution time: {time.time()-start_time:.2f} seconds")
