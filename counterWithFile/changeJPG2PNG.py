import os, glob
import cv2
from PIL import Image
def resizeAllFile(folder):
    for file in os.listdir(folder):
        img = Image.open(folder + '/' + file)
        print(folder + '/' + file[:-4] + '.png')
        img = img.save(folder + '/' + file[:len(file)-4] + '.png')
    for i in glob.glob(folder + "\\*.jpg"):
        os.remove(i)
resizeAllFile("result")
