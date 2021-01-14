import os
import cv2
def resize(img):
    
    return 
def resizeAllFile(folder):
    dim = (256,256)
    for file in os.listdir(folder):
        img = cv2.imread(folder + '\\' + file)
        img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        cv2.imwrite(folder + '\\' + file, resize(img))

resizeAllFile("C:\\Users\\haime\\Downloads\\result")