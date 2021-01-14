import cv2
import matplotlib.pyplot as plt
from changeBrightness import changeH, changeS, changeV 

def changeImage(img, s, v):
    return changeV(changeS(img, s), v)
def findHSV(img, img2):
    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    hist2 = cv2.calcHist([img2],[0],None,[256],[0,256]) 
    minHist = abs(cv2.compareHist(hist, hist2, cv2.HISTCMP_CORREL))
    minJ, minK = 0,0
    for j in range(0, 255,5):
            for k in range(0, 255,5):
                changedImage = changeImage(img2, j, k)
                changedHist = cv2.calcHist([changedImage],[0],None,[256],[0,256]) 
                if minHist > abs(cv2.compareHist(hist, changedHist, cv2.HISTCMP_CORREL)):
                    minHist = abs(cv2.compareHist(hist, changedHist, cv2.HISTCMP_CORREL))
                    minJ = j
                    minK = k   
    print(f"Changed: {minJ}, {minK}")
    return changedImage, minHist

img = cv2.imread("epoch004_real_A.png")
img2 = cv2.imread("epoch004_fake_B.png")
changedImage, minHist = findHSV(img, img2)

hist = cv2.calcHist([img],[0],None,[256],[0,256])
changedHist = cv2.calcHist([changedImage],[0],None,[256],[0,256]) 
plt.subplot(2,1,1)
plt.plot(hist) 

plt.subplot(2,1,2)
plt.plot(changedHist) 
plt.show()
print(minHist)
cv2.imshow("origin", img)
cv2.imshow("changed", changedImage)
cv2.waitKey(0)  
cv2.destroyAllWindows()  