import cv2 as cv

#import image as pixel matrix
img = cv.imread("Photos/cat_large.jpg")

#imshow(window name, pixel matrix)
cv.imshow("cat", img)

#waits time in miliseconds for a key to be pressed, 0 means infinite
cv.waitKey(0)