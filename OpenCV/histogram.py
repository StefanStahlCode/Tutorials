import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("Photos/cats.jpg")
#cv.imshow("control", img)

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("grey", grey)

#mask for histogram
blank = np.zeros(img.shape[:2], dtype='uint8')

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)


masked = cv.bitwise_and(grey, grey, mask=mask)
#cv.imshow("mask", masked)

#greyscale histogram
#list of images, list of channels, mask, histsize, range of pixel values
# grey_hist = cv.calcHist([grey], [0], None, [256], [0,256])
# plt.figure()
# plt.title("Greyscale Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of pixels")
# plt.plot(grey_hist)
# plt.xlim([0, 256])
# plt.show()

#color histogram

plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")


colors = ("b", "g", "r")
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)