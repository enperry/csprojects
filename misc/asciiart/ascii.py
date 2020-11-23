from PIL import Image
import subprocess
from colorama import Fore, Style

ASCIIChars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
maxPixelValue = 256

def getPixelMatrix(img, height):
    img.thumbnail((height, 200))
    pixels = list(img.getdata())
    return [pixels[i:i+img.width] for i in range(0, len(pixels), img.width)]

def getIntensityMatrix(pixelsMatrix, algoName = "average"):
    intensityMatrix = []
    for row in pixelsMatrix:
        intensityRow = []
        for p in row:
            if(algoName == "average"):
                intensity = (p[0] + p[1] + p[2] / 3.0)
            elif (algoName == 'max_min'):
                intensity = (max(p) + min(p) / 2.0)
            elif (algoName == 'luminosity'):
                intensity = 0.21*p[0] + 0.72*p[1] + 0.07*p[2]
            else:
                raise Exception("Unrecognixed algoName: %s" % algoName)
            intensityRow.append(intensity)
        intensityMatrix.append(intensityRow)
    return intensityMatrix

def normalizeIntensityMatrix(intensityMatrix):
    normalizedIntensityMatrix = []
    maxPixel = max(map(max, intensityMatrix))
    minPixel = min(map(max, intensityMatrix))
    for row in intensityMatrix:
        rescaledRow = []
        for p in row:
            r = maxPixelValue * (p - minPixel) / float(maxPixel - minPixel)
            rescaledRow.append(r)
        normalizedIntensityMatrix.append(rescaledRow)
    
    return normalizedIntensityMatrix

def invertIntensityMatrix(intensityMatrix, ASCIIChars):
    invertedIntensityMatrix = []
    for row in intensityMatrix:
        invertedRow = []
        for p in row:
            invertedRow.append(maxPixelValue - p)
        invertedIntensityMatrix.append(invertedRow)
    
    return invertedIntensityMatrix

def convertToASCII(intensityMatrix, ASCIIChars):
        ASCIIMatrix = []
        for row in intensityMatrix:
            ASCIIRow = []
            for p in row:
                ASCIIRow.append(ASCIIChars[int(p/maxPixelValue * len(ASCIIChars)) - 1])
            ASCIIMatrix.append(ASCIIRow)
        
        return ASCIIMatrix
    
def printASCIIMatrix(ASCIIMatrix, textColor):
    for row in ASCIIMatrix:
        line = [p + p + p for p in row]
        print(textColor + "".join(line))

    print(Style.RESET_ALL)

filepath = "/Users/kuro/Desktop/school/cs projects/asciiart/Capture_2020-06-27-14-31-50.png"
subprocess.call(["imagesnap", filepath, "-w", "2"])

img = Image.open(filepath)
pixels = getPixelMatrix(img, 100)

intensityMatrix = getIntensityMatrix(pixels, "luminosity")
intensityMatrix = normalizeIntensityMatrix(intensityMatrix)

asciiMatrix = convertToASCII(intensityMatrix, ASCIIChars)
printASCIIMatrix = (asciiMatrix, Fore.GREEN)