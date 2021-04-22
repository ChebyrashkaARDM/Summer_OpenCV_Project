import cv2
import numpy as np

frameWidth = 128
frameHeight = 128
cap = cv2.VideoCapture(0)


def empty(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 480, 240)
cv2.createTrackbar("HUE Min", "HSV", 0, 255, empty)
cv2.createTrackbar("Sat Min", "HSV", 0, 255, empty)
cv2.createTrackbar("Value Min", "HSV", 0, 255, empty)
cv2.createTrackbar("HUE Max", "HSV", 255, 255, empty)
cv2.createTrackbar("Sat Max", "HSV", 255, 255, empty)
cv2.createTrackbar("Value Max", "HSV", 255, 255, empty)

while True:

    _, img = cap.read()
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("HUE Min", "HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_min = cv2.getTrackbarPos("Sat Min", "HSV")
    s_max = cv2.getTrackbarPos("Sat Max", "HSV")
    v_min = cv2.getTrackbarPos("Value Min", "HSV")
    v_max = cv2.getTrackbarPos("Value Max", "HSV")
    print(h_min)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask = mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img, mask, result])
    cv2.imshow("Stack", hStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()