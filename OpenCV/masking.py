import cv2 as cv
import numpy as np

img = cv.imread("Photos/cats.jpg")
cv.imshow("cats", img)

#mask needs to be same size as original image
blank = np.zeros(img.shape[:2], dtype="uint8")

mask = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
#cv.imshow("Mask", mask)

masked = cv.bitwise_and(img, img, mask=mask)
#cv.imshow("masked", masked)

rectangle = cv.rectangle(blank.copy(), (20, 100),(300, 300), 255, -1)
#cv.imshow("rectangle", rectangle)


test_shape = cv.bitwise_and(mask, rectangle)
#cv.imshow("test_shape", test_shape)
masked_2 = cv.bitwise_and(img, img, mask=test_shape)
cv.imshow("masked test", masked_2)

cv.waitKey(0)