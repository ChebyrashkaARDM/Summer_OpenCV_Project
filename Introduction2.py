import cv2

img = cv2.imread("Src/Example.jpg")
print(img.shape)

imgResize = cv2.resize(img, (512, 512))
print(imgResize.shape)

cv2.imshow("Image", img)
cv2.imshow("Resize Image", imgResize)

cv2.waitKey(0)