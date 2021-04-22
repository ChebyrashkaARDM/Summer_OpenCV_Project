import cv2
import numpy as np

crown = cv2.imread("Src/Crown.jpg")
crown = cv2.resize(crown, (450,250))
smile = cv2.imread("Src/Smile.png")
smile = cv2.resize(smile, (450, 460))

result = np.vstack((crown, smile))

cv2.imshow("Crown", crown)
cv2.imshow("Smile", smile)
cv2.imshow("Result", result)

cv2.waitKey(0)