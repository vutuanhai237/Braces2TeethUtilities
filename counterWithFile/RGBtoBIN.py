import os
import cv2, copy
import numpy as np
def convertToBin(img):
    copyImg = copy.copy(img)
    for i in range(0, copyImg.shape[0]):
        for j in range(0, copyImg.shape[1] ):
            gsc = 0.3*copyImg[i,j,0] + 0.59*copyImg[i,j,1] + 0.11*copyImg[i,j,2]
            copyImg[i,j,:] = [gsc, gsc, gsc]
    return copyImg
def process(folder):
    for file in os.listdir(folder):
        img = cv2.imread(folder + '/' + file)
        img = cv2.resize(img, (256,256), interpolation = cv2.INTER_CUBIC)
        #cv2.imshow(file + "s", img)
        img2 = convertToBin(img)
        img2 = np.concatenate((img, img2), axis=1)  
        cv2.imwrite(folder + '/' + file, img2)

process("C:/Users/haime/Downloads/Dataset/colorToBinary/1001 - 2000")
cv2.waitKey()