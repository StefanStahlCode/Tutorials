import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
#documentation:
#gradients: https://docs.opencv.org/4.x/d5/d0f/tutorial_py_gradients.html
#edge detetcion: https://learnopencv.com/edge-detection-using-opencv/
img = cv.imread("Photos/cats.jpg")
cv.imshow("control", img)

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', grey)

# Laplacian
lap = cv.Laplacian(grey, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel 
sobelx = cv.Sobel(grey, cv.CV_64F, 1, 0)
sobely = cv.Sobel(grey, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

canny = cv.Canny(grey, 150, 175)
cv.imshow('Canny', canny)






cv.waitKey(0)