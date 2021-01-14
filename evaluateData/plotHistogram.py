# importing required libraries of opencv
import cv2
import glob
import random as rd
from scipy.stats import wasserstein_distance 
import numpy as np
from matplotlib import pyplot as plt



hist_success, hist_failure = [], []
def showMultiPlot(path, color, title, i):
    list_images = [cv2.imread(file) for file in glob.glob(path)]
    print(list_images[0].shape)
    images = []
    for i in range(0, 50):
        images.append(rd.choice(list_images))
    # find frequency of pixels in range 0-255
    hists = []
    for img in images:
        hists.append(cv2.calcHist([img], [0], None, [256], [0, 256]))

    plt.plot(sum(hists) / len(hists), color=color, label=title)
    if title == "success":
        plt.savefig(f"./random_hist/success_{i}.png")
        
    else:
        plt.savefig(f"./random_hist/failure_{i}.png")
    return sum(hists) / len(hists)
    
w_hist = []
for i in range(0, 50):
    hist_success = np.array(showMultiPlot("./crop_mouth/success/*.png", "green", "success", i))
    hist_failure = showMultiPlot("./crop_mouth/failure/*.png", "red", "failure", i)
    #w_hist.append(wasserstein_distance(hist_success, hist_failure))
print(hist_success)
plt.legend()
plt.show()
