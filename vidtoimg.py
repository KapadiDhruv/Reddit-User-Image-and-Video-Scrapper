import cv2
import os

# Define the input and output paths
video_path = 'petite-love/pics_petite-love.avi'
output_dir = 'petite-love/output_images'

# Create the output directory if it does not exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Open the video file
video = cv2.VideoCapture(video_path)

# Loop through each frame in the video and save it as an image
frame_number = 0
while True:
    # Read the next frame from the video
    ret, frame = video.read()
    
    # If there are no more frames, break out of the loop
    if not ret:
        break
    
    # Save the current frame as an image in the output directory
    image_filename = os.path.join(output_dir, f'frame_{frame_number:04d}.jpg')
    cv2.imwrite(image_filename, frame)
    
    # Increment the frame counter
    frame_number += 1

# Release the video object and close any open windows
video.release()
cv2.destroyAllWindows()
