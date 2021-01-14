import sys
import getopt
import cv2
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import math
import functools
from genTeethColor import isTeethColor, findTeethColor, readTeethShade
import collections 

class Superpixel():
    def __init__(self):
        self.name = ''
        self.pixels = []
        self.id = None
        self.meanDensity = None
        self.replaceColor = None

    def setReplaceColor(self, replaceColor):
        self.replaceColor = replaceColor
    def getReplaceColor(self):
        return self.replaceColor

    def setMeanDensity(self, meanDensity):
        self.meanDensity = meanDensity

    def setID(self, id):
        self.id = id

    def getID(self):
        return self.id

    def addPixel(self, pixel):
        self.pixels.append(pixel)

    def getPixel(self):
        return self.pixels

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def getMeanDensity(self):
        if self.meanDensity is not None:
            return self.meanDensity
        result = [0, 0, 0]
        for pixel in self.pixels:
            result[0] = result[0] + pixel[0][0]
            result[1] = result[1] + pixel[0][1]
            result[2] = result[2] + pixel[0][2]
        result[0] = round(result[0] / len(self.pixels))
        result[1] = round(result[1] / len(self.pixels))
        result[2] = round(result[2] / len(self.pixels))
        return result
    def getNumberOfPixels(self):
        return len(self.pixels)

    def __str__(self):
        return f"Name: {self.name}, ID: {self.id}, numOfPixel: {len(self.pixels)}"


def genSuperpixelSEED(image):
    numberOfSuperpixel = 500
    iterator = 100
    blockLevels = 10
    seeds = cv2.ximgproc.createSuperpixelSEEDS(
        image.shape[1], image.shape[0], image.shape[2], numberOfSuperpixel, blockLevels, prior=2, histogram_bins=5, double_step=False)
    seeds.iterate(image, num_iterations=iterator)
    return seeds


def getSuperpixels(image, labels, numberOfSuperpixelResult):
    superpixels = []
    for i in range(0, numberOfSuperpixelResult):
        newSuperpixel = Superpixel()
        newSuperpixel.setID(i)
        superpixels.append(newSuperpixel)
    for i in range(0, labels.shape[0]):
        for j in range(0, labels.shape[1]):
            superpixels[labels[i][j]].addPixel((image[i][j], i, j))
    return superpixels


def genSuperpixelSLIC(image, regionSize):
    SLIC = 100
    SLICO = 101
    num_iter = 100
    slics = cv2.ximgproc.createSuperpixelSLIC(
        image, region_size=regionSize, ruler=20.0)
    slics.iterate(num_iterations=num_iter)

    return slics


def genSuperpixelLSC(image, regionSize):
    SLIC = 100
    SLICO = 101
    num_iter = 100
    slcs = cv2.ximgproc.createSuperpixelLSC(image, region_size=regionSize)
    slcs.iterate(num_iter)
    return slcs


def preProcessing(image, teethColor):
    seeds = genSuperpixelSEED(image)
    numberOfSuperpixelResult = seeds.getNumberOfSuperpixels()
    labels = seeds.getLabels()
    superpixels = getSuperpixels(image, labels, numberOfSuperpixelResult)
    for superpixel in superpixels:
        density = superpixel.getMeanDensity()
        if isTeethColor([density[2], density[1], density[0]], teethColor, 20):
            superpixel.setName("teeth")
        else:
            superpixel.setName("notTeeth")

    getColorNeighboor(image, superpixels, labels, numberOfSuperpixelResult)
    for i in range(0, labels.shape[0]):
        for j in range(0, labels.shape[1]):
            if superpixels[labels[i][j]].getName() == "notTeeth":
                replaceColor = superpixels[labels[i][j]].getReplaceColor()
                image[i][j] = [replaceColor[2], replaceColor[1], replaceColor[0]]     
    return image


def getColorNeighboor(image, superpixels, labels, numberOfSuperpixelResult):
    for i in range(0, numberOfSuperpixelResult):
        if superpixels[i].getName() == "notTeeth":
            findTeethColorForSuperpixel(image, labels, superpixels, i)
    
            
def findTeethColorForSuperpixel(image, labels, superpixels, id):
    pixels = superpixels[id].getPixel()
    pixelsX = []
    pixelsY = []
    for pixel in pixels:
        pixelsX.append(pixel[1])
        pixelsY.append(pixel[2])
    topLeft = (min(pixelsX), min(pixelsY))
    botRight = (max(pixelsX), max(pixelsY))
    pixelMayBeTeeths = []
    for i in range(topLeft[0], botRight[0]):
        for j in range(topLeft[1], botRight[1]):
            if superpixels[labels[i][j]].getName() == "notTeeth":
                pixelMayBeTeeths.append(image[i][j])
    teethShades = readTeethShade()
    superpixels[id].setReplaceColor(findTeethColor(pixelMayBeTeeths, teethShades).getColor())