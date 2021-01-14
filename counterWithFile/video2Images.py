import cv2

def video2Images(pathOfVideo, folder):
    vidcap = cv2.VideoCapture(pathOfVideo)
    success,image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite(folder + '\\frame%d.png' % count, image) 
        success, image = vidcap.read()
        count += 1