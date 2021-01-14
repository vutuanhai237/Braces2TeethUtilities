video_name = "video.avi"
import os
import moviepy.video.io.ImageSequenceClip

image_folder = "C:\\Users\\haime\\OneDrive\\Documents\\GitHub\\Braces2TeethServer\\results\\braces2teeth\\test_latest\\images\\result"
fps = 30

image_files = [
    image_folder + "/" + img for img in os.listdir(image_folder) if img.endswith(".png")
]
clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
clip.write_videofile("my_video2.mp4")

