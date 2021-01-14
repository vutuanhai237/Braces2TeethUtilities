import os
import cv2
import glob
import random as rd
import sys, argparse

parsers = argparse.ArgumentParser()
parsers.add_argument("-f", "--folder", help="Please enter folder path")
args = parsers.parse_args()
def changeV(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] = v[v <= lim] + value
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

def changeS(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    lim = 255 - value
    s[s > lim] = 255
    s[s <= lim] = s[s <= lim] + value
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

def genImageByChangeSV(img, imgName, numOfGenImage):
    genImages = []
    for i in range(0, numOfGenImage):
        newS = rd.randint(0, 100)
        newV = rd.randint(0, 255)
        newImage = changeS(changeV(img, newV), newS)
        genImages.append(newImage)
        cv2.imwrite(os.path.join(args.folder , imgName[:imgName.find('.')]  + "_" + str(i) + ".png"), newImage)
    return genImages

images = [cv2.imread(file) for file in glob.glob(f"{args.folder}/*.png")]

fileName = os.listdir(args.folder)

for i in range(0, len(images)):
    genImageByChangeSV(images[i], fileName[i], 7)

print(args.folder)
