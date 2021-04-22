import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)

img = cv2.imread("Src/Example.jpg")
imgCanny = cv2.Canny(img, 130, 130)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilate Image", imgDilation)
cv2.imshow("Erode Image", imgEroded)

cv2.waitKey(0)