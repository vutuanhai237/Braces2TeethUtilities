from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2
import copy
import colorsys
import math
import os
import shutil
import collections 
from convexHull import convexHull, convexRectangle 
from processBar import progressbar
from genTeethColor import findTeethColor, readTeethShade, getListPixelMayBeTeeth

from genSuperpixel import preProcessing

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def getFacial(image):
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 1)
    for (i, rect) in enumerate(rects):
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        (x, y, w, h) = face_utils.rect_to_bb(rect)
        return shape[60:68]
        




def distance(p1, p2):
    upperCos = p1[0]*p2[0] + p1[1] * p2[1] + p1[2]*p2[2]
    lowerCos = (p1[0]**2+p1[1]**2+p1[2]**2)**(1/2) * (p2[0]**2+p2[1]**2+p2[2]**2)**(1/2)  
    acos = math.acos((upperCos/lowerCos))*180/math.pi
    return acos

def calculateThreshhold(image, color):
    distances = []
    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):
            pixel = image[i][j]
            distances.append(distance(pixel, color))
    distances.sort()
    return distances[int(len(distances)*0.5)]



def shiftShapeAfterCrop(shape, point):
    result = []
    for p in shape:
        result.append([p[0] - point[0], p[1] - point[1]])
    return np.array([result], np.int32)


def reInpainting(image, groundTruth, teethColor):
    """
        if pixel has pink color (marked for teeth) and not in range of teeth => fill by teethColor
    """
    preProcessedImage = preProcessing(image, teethColor)

    #print(list(preProcessedImage[0][0]))
    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):
            pixel = image[i][j]
            pink = [255, 0, 255]
            if collections.Counter(pixel) == collections.Counter(pink):
                #print( preProcessedImage[i][j])
                print(groundTruth[i, j])
                groundTruth[i, j] = [preProcessedImage[i, j][0], preProcessedImage[i, j][1], preProcessedImage[i, j][2]]
    return groundTruth

def createFacial(image):
    try:
        shape = getFacial(image) # points of mouth
        if shape is None:
            return None
        else:
            [topLeft, botRight] = convexRectangle(shape) # 2 point for crop mouth
            needed_image = copy.copy(image)
            if topLeft[1] - botRight[1] > topLeft[0] - botRight[0]:
                deltaXY = abs(abs(topLeft[1] - botRight[1]) - abs(topLeft[0] - botRight[0]))
                newTopLeft = [topLeft[0], topLeft[1] - int(deltaXY/2)]
                newBotRight = [botRight[0], botRight[1] + int(deltaXY/2)]
                upper_needed_image = needed_image[newTopLeft[1] : topLeft[1] + 1, newTopLeft[0] : botRight[0] + 1]
                bottom_needed_image = needed_image[botRight[1] : newBotRight[1] + 1, newTopLeft[0] : botRight[0] + 1]
                needed_image = needed_image[newTopLeft[1] : newBotRight[1] + 1, newTopLeft[0] : newBotRight[0] + 1]
            image = image[topLeft[1] : botRight[1] + 1, topLeft[0] : botRight[0] + 1] # mouth
            shape = shiftShapeAfterCrop(shape, topLeft) # new point of mouth after crop
            groundTruth = copy.copy(image)
            pixelMayBeTeeths = getListPixelMayBeTeeth(image) # color on +
            teethShades = readTeethShade() # list of teeth shade
            teethColor = findTeethColor(pixelMayBeTeeths,teethShades).getColor() # color of teeth
            image = convexHull(image, shape)
            groundTruth = reInpainting(image, groundTruth, teethColor)
            image = cv2.resize(image, (256,256), interpolation = cv2.INTER_CUBIC)
            res = np.concatenate((upper_needed_image, groundTruth, bottom_needed_image), axis=0)  
            res = cv2.resize(res, (256,256), interpolation = cv2.INTER_CUBIC )
            needed_image = cv2.resize(needed_image, (256,256), interpolation = cv2.INTER_CUBIC )
            out = np.concatenate((needed_image, res), axis=1)
            return out
    except:
        return
def make_directory_if_not_exists(path):
    while not os.path.isdir(path):
        try:
            os.makedirs(path)
            break    
        except WindowsError:
            print("got WindowsError")
            pass       
def main():
    path = "C:/Users/haime/Downloads/test1"
    shutil.rmtree(path + "/result", ignore_errors=True)
    os.mkdir(path + "/result")
    files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    for i in progressbar(range(len(files)), "Computing: ", 10):
        file = files[i]
        filename = file.split(".")
        images = cv2.imread(path + '/' + file)
        out = createFacial(images)
        if out is not None:
            cv2.imwrite(f"{path}/result/{filename[0]}.png", out)

if __name__ == "__main__":
    main()