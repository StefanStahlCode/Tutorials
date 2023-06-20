import cv2 as cv
import numpy as np


#more information on rotation and translation: https://docs.opencv.org/3.4/d4/d61/tutorial_warp_affine.html
img = cv.imread("Photos/park.jpg")
cv.imshow("park", img)

#translation
#shifting along x or y axis
#making translation matrix


def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    #source, tranlation matrix, dimension
    return cv.warpAffine(img, transMat, dimensions)

#x axis: left(-) to right(+)
#y axis: up(-) to down(+)

translated = translate(img, 100, 100)
cv.imshow("translated", translated)


#rotation
#image, angle, rotation point
def rotate(img, angle, point=None):
    (height, width) = img.shape[:2]

    if point == None:
        point = (width//2, height//2)
    
    #rotation point, angle, scale
    rotMat = cv.getRotationMatrix2D(point, angle, 1.0)
    dimension = (width, height)

    return cv.warpAffine(img, rotMat, dimension)

#-angle for clockwise rotation
rotated = rotate(img, 69)
cv.imshow("rotated", rotated)

#rotating a rotated image is possible, but not advised






cv.waitKey(0)