import cv2 as cv
import numpy as np

#using a numpy matrix as pixel matrix
#height, width, color channels
blank = np.zeros((500, 500, 3), dtype = "uint8")
#cv.imshow("blank", blank)


#paint the image a certain color
#using rgb (blue, green, red) to set color values
blank[:] = 255,0,0
#using a range of pixels
#blank[10:200, 100:300] = 100, 169,0
#blank[300:500, 250:500] = 0, 200, 150

#making a rectangle
#(image, point1=orign(width, height), end, color, thickness)
#thickness of lines, use either cv.filled or -1 for a filled rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,0,255), thickness=-1 )
#cv.imshow("Rectangle", blank)



#drawing circle
#(image, center, radius, color, thickness)
cv.circle(blank, (blank.shape[1]//4, blank.shape[0]//4), 100, (100,100,100), thickness=-1)
#cv.imshow("circle", blank)

#draw line
#image, start point, end point, color, thickness
cv.line(blank, (blank.shape[1]//2, 0), (blank.shape[1]//2, blank.shape[0]), (255,255,255), thickness=3)
#cv.imshow("not blank", blank)

#writing text
#addtext has some use for Qt GUIs, putText is usually used
#(image, text, origin (left to right, up to down), fontface, fontscale, color, thickness)
cv.putText(blank, "Hello", (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,255), thickness=2)
cv.imshow("text with everything", blank)







cv.waitKey(0)