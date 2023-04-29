import cv2
import os

# Define the input and output paths
image_dir  = 'petite-love/pics_petite-love'

# Define the frame rate of the output video
fps = 1

image_filenames = sorted(os.listdir(image_dir))

# Set the dimensions of the output video to match the dimensions of the first image
img = cv2.imread(os.path.join(image_dir, image_filenames[0]))
height, width, channels = img.shape

# Define the video writer object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_out = cv2.VideoWriter('petite-love/pics_petite-love.mp4', fourcc, fps, (width, height))

# Loop through each image in the directory and add it to the video writer
for image_filename in image_filenames:
    img = cv2.imread(os.path.join(image_dir, image_filename))
    
    # Resize the image to match the video dimensions and maintain the aspect ratio
    img = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
    
    # Write the image to the video writer
    video_out.write(img)
    
    # Wait for one second before processing the next image
    cv2.waitKey(1000)

# Release the video writer and close any open windows
video_out.release()
cv2.destroyAllWindows()