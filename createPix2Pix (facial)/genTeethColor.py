
from colorDistance import CIEDE2000
class Shade:
    def __init__(self, code, r, g, b):
        self.code = code
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return f"Code: {self.code}, Color: RGB({self.r}, {self.g}, {self.b})"

    def getCode(self):
        return self.code

    def getColor(self):
        return [int(self.r), int(self.g), int(self.b)]

def getListPixelMayBeTeeth(image):
    vertical = image[int(image.shape[0] / 2), :] 
    horizontal =  image[:, int(image.shape[1] / 2)]
    listPixel = []
    for color in horizontal:
        listPixel.append(color)
    for color in vertical:
        listPixel.append(color)
    return listPixel
    
def readTeethShade():
    file = open(
        r"C:\Users\haime\OneDrive\Máy tính\Python\facial\teethcolor.txt",
        "r",
        encoding="utf8",
    )
    outString = []
    for line in file:
        line = line.rstrip("\r\n")
        line = line.split(",")
        outString.append(Shade(line[0], line[1], line[2], line[3]))
    return outString

def findTeethColor(pixelMayBeTeeths, teethShades):
    minShade = teethShades[0]
    minMayBeTeeth = pixelMayBeTeeths[0]
    minDist = CIEDE2000(pixelMayBeTeeths[0], teethShades[0].getColor())
    for teethColor in pixelMayBeTeeths:
        for shade in teethShades:
            dist = CIEDE2000(teethColor, shade.getColor())
            if dist - minDist < 0:
                minShade = shade
                minDist = dist
                minMayBeTeeth = teethColor
    return minShade

def isTeethColor(pixel, teethColor, threshold):
    """
        if pixel is so close to teeth color, return true
    """
    if CIEDE2000(pixel, teethColor) < 10:
        return True
    return False