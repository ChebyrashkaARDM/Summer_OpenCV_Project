import cv2

image = cv2.imread("Src/cat.jpg")
cv2.imshow("Image", image)
print(image.shape)

part1 = image[0:200, 200:500]
cv2.imshow("1", part1)

part2 = image[200:400, 0:200]
cv2.imshow("2", part2)

part3 = image[0:550, 720:900]
cv2.imshow("3", part3)

cv2.waitKey(0)