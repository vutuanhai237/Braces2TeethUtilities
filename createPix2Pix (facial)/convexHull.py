import cv2
import numpy as np
def convexHull(image, shape):
    image = cv2.fillPoly(image, [shape], (255, 0, 255))
    return image
def convexRectangle(countours):
    xs, ys = [], []
    if countours is None:
        return [[0,0],[0,0]]
    for point in countours:
        xs.append(point[0])
        ys.append(point[1])
    minX = np.min(xs)
    minY = np.min(ys)
    maxX = np.max(xs)
    maxY = np.max(ys)
    return [[int(minX), int(minY)], [int(maxX), int(maxY)]]