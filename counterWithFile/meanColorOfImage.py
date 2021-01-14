import cv2
import numpy as np
import os
path = "C:/Users/haime/Downloads/Vita3DMasterRGB"

for file in os.listdir(path):
    img = cv2.imread(path + '/' + file)

    average = img.mean(axis=0).mean(axis=0)
    print(file[0:len(file)-4] + "," + str(int(average[0])) + "," + str(int(average[1]))+ "," + str(int(average[2])))