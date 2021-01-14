import cv2
import numpy as np
img = cv2.imread("images/braces.png") # BRG order, uint8 type
cv2.imshow('ImageWindow', img)
converted_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.waitKey(0)
num_superpixels = 200  # desired number of superpixels
num_iterations = 4     # number of pixel level iterations. The higher, the better quality
prior = 2              # for shape smoothing term. must be [0, 5]
num_levels = 4
num_histogram_bins = 5 # number of histogram bins
height, width, channels = converted_img.shape
seeds = cv2.ximgproc.createSuperpixelSEEDS(width, height, channels, num_superpixels, num_levels, prior, num_histogram_bins)
seeds.iterate(converted_img, num_iterations)
labels = seeds.getLabels() #
mask = seeds.getLabelContourMask(False)
cv2.imshow('MaskWindow', mask)
cv2.waitKey(0)
color_img = np.zeros((height, width, 3), np.uint8)
color_img[:] = (0, 0, 255)
mask_inv = cv2.bitwise_not(mask)
result_bg = cv2.bitwise_and(img, img, mask=mask_inv)
result_fg = cv2.bitwise_and(color_img, color_img, mask=mask)
result = cv2.add(result_bg, result_fg)
cv2.imshow('ColorCodedWindow', result)
cv2.waitKey(0)


cv2.destroyAllWindows()