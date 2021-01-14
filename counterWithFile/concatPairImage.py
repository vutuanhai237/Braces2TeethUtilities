import cv2
import numpy as np
import os, glob
from PIL import Image
def getConcat(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def concatPairImage(folder):
    lists = glob.glob(folder + '/*.png')
    subList = [lists[n:n+2] for n in range(0, len(lists), 2)]
    for files in subList:
        fake = Image.open(files[0])
        real = Image.open(files[1])
        number = int(((files[0].split('\\'))[-1])[5:-9])
        index = ''
        if number < 10:
            index = '00' + str(number)
        elif number < 100:
            index = '0' + str(number)
        else:
            index = str(number)
        getConcat(real, fake).save(folder + '\\result\\' + index + '.png')


concatPairImage('C:\\Users\\haime\\OneDrive\\Documents\\GitHub\\Braces2TeethServer\\results\\braces2teeth\\test_latest\\images')

# concatPairImage('C:\\Users\\haime\\Downloads\\result')
