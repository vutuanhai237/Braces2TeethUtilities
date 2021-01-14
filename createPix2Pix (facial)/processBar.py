import sys
import time
import numpy as np
import cv2
def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i - %d %s\r" % (prefix, "#"*x, "."*(size-x), j, count, int(j/count*100), '%'))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()


# progressbar((10), "Computing: ", 10)
# progressbar((100), "Computing: ", 10)
# for i in progressbar(range(10), "Computing: ", 10):
#     image = cv2.imread("C:/Users/haime/Downloads/test/1.png")
#     cv2.imwrite("hai.png", image)
