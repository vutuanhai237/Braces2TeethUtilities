import cv2
import matplotlib.pyplot as plt

# cv2.namedWindow("Color Track Bar")

def changeV(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] = v[v <= lim] + value
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img
def changeH(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    lim = 255 - value
    h[h > lim] = 255
    h[h <= lim] = h[h <= lim] + value
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
# def on_trackbar(val):
#     pass


# img = cv2.imread("epoch004_fake_B.png")
# cv2.createTrackbar("h", "Color Track Bar", 50, 255, on_trackbar)
# cv2.createTrackbar("s", "Color Track Bar", 50, 255, on_trackbar)
# cv2.createTrackbar("v", "Color Track Bar", 50, 255, on_trackbar)

# while True:
#     h = cv2.getTrackbarPos("h", "Color Track Bar")
#     s = cv2.getTrackbarPos("s", "Color Track Bar")
#     v = cv2.getTrackbarPos("v", "Color Track Bar")

#     newImageH = changeH(img, int(h))
#     newImageS = changeS(newImageH, int(s))
#     newImageV = changeV(newImageS, int(v))
#     cv2.imshow("v", newImageV)
    
#     if cv2.waitKey(1) == 27:
#         break
# cv2.destroyAllWindows()

