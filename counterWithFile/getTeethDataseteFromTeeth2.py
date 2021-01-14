import os
import cv2
def getHalf(folder):
    for file in os.listdir(folder):
        image = cv2.imread(folder + '/' + file)
        img = image[:, :int(image.shape[1]/2), :]
        cv2.imwrite(folder + '/' + file, img)

getHalf("C:/Users/haime/Downloads/crawler/teeth2/test")
