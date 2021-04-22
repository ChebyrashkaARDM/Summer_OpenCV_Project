import cv2

image = cv2.imread("Src/Politician_Coordinates.jpg")

cv2.line(image, (357, 0), (357,720), (0, 0, 0), 3)
cv2.line(image, (0, 380), (720,380), (0, 0, 0), 3)

cv2.rectangle(image,(13, 86), (189, 235), (66, 196, 149), 2)
cv2.rectangle(image,(365, 65), (548, 227), (153, 65, 78), 2)
cv2.rectangle(image,(20, 417), (186, 559), (98, 58, 217), 2)
cv2.rectangle(image, (376, 391),(573, 561), (64, 236, 234), 2)

cv2.circle(image, (357, 380), 5, (128, 128, 128), 20)

cv2.putText(image, ("Gosling's Coordinates"), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

cv2.imshow("Image", image)

cv2.waitKey(0)