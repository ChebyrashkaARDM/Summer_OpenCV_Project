import cv2
import numpy as np

img1 = cv2.imread("Src/Apple.png")
img1 = cv2.resize(img1, (200, 200))
img2 = cv2.imread("Src/Pineapple.png")
img2 = cv2.resize(img2, (200, 200))

cv2.imshow("Apple", img1)
cv2.imshow("PineApple", img2)

pineApple = np.hstack((img1, img2))

cv2.imshow("ApplePineAppple", pineApple)

cv2.waitKey(0)