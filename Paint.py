import cv2
import numpy as np

frameWidth = 1920
frameHeight = 1080
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

myColors = [#[60, 60, 0, 88, 255, 255],              #green
            [19, 85, 0, 80, 255, 255],              #yellow
            [63, 135, 0, 255, 255, 255],            #purple
            #[0, 161, 0, 229, 255, 255]              #orange
            ]

myColorsValues = [#[0, 128, 0],
                  [0, 255, 255],
                  [133, 21, 199],
                  #[0, 165, 255]
                  ]

myPoints = []               #[x, y, colorId]

def colorFinding(img, myColors, myColorsValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgResult, (x, y), 10, myColorsValues[count], cv2.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x, y, count])
        count += 1
        cv2.imshow("Mask", mask)
    return newPoints

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + w//2, y

def drawOnCanvas(myPoints, myColorsValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorsValues[point[2]], cv2.FILLED)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    #imgResult = cv2.flip(imgResult, 1)
    newPoints = colorFinding(img, myColors, myColorsValues)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorsValues)
    cv2.imshow("Camera", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
