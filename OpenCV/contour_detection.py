import cv2 as cv
import numpy as np

img= cv.imread("Photos/cats.jpg")

blank = np.zeros(img.shape, dtype="uint8")



gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)


#edges and contour are different
#comparison
#canny = cv.Canny(img, 125, 175)
#cv.imshow("canny", canny)

#https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
#turns image into a binary image
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("thresh", thresh)

#different types of contours can be returned, cv.retr_list returns all
#https://docs.opencv.org/4.x/d4/d73/tutorial_py_contours_begin.html
#CHAIN_APPROX_SIMPLE compressed contours into simpler ones
#CHAIN_APPROX_NONE does nothing to the returned contours
contours, hierachies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
#numbe rof contours found
print(len(contours))
#note: blurring an image drasdtically reduced the contours of an image

#drawing contours on blank image
#image to draw, contour list, -1-> all contours, color in blue green red, thickness
cv.drawContours(blank, contours, -1, (255,0,255), 1)
cv.imshow("contours drawn", blank)




cv.waitKey(0)