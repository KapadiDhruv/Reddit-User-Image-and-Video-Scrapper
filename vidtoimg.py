import cv2
import os

with open("sub_list.csv", "r") as f_subreddits:
    for sub in f_subreddits:
        sub = sub.strip()
        username = sub

    # Path to the video file
    vid_path = f'{username}/{username}.mkv'

    # Create a folder to store the extracted images
    img_folder = f'{username}/thepics_{username}'
    if not os.path.exists(img_folder):
        os.makedirs(img_folder)

    # Open the video file
    vidcap = cv2.VideoCapture(vid_path)

    # Get the frame rate of the video
    fps = vidcap.get(cv2.CAP_PROP_FPS)

    # Loop through the frames and extract them as images
    success, image = vidcap.read()
    count = 0
    while success:
        img_name = f"frame{count:05d}.png"
        img_path = os.path.join(img_folder, img_name)
        cv2.imwrite(img_path, image, [cv2.IMWRITE_PNG_COMPRESSION, 0])
        success, image = vidcap.read()
        count += 1

    # Release the video and close all windows
    vidcap.release()
    cv2.destroyAllWindows()


