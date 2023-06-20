import cv2 as cv

#blue, green, red image
img = cv.imread("Photos/park.jpg")

#cv.imshow("park", img)

#convertig image to greyscaled
#image, colorcode
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("Gray", gray)

#blur
#here only gaussian blur
#source image, kernel size(needs to be odd number)
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
#cv.imshow("Blur", blur)


#edge cascade
#source, threshold 1, threshold 2
canny = cv.Canny(img, 125, 175)
#cv.imshow("canny", canny)

#reducing edges by blurring
canny2 = cv.Canny(blur, 125, 175)
#cv.imshow("canny2", canny2)


#dilating the image
#source, kernel, 
dilated = cv.dilate(canny2, (7,7), iterations=3)
#cv.imshow("dilated", dilated)


#eroding 
eroded = cv.erode(dilated, (7,7), iterations=3)
#cv.imshow("eroded", eroded)

#resize
#image, destination size
#ignoring aspect ratio
#interpolation default= cv.INTER_AREA, useful for shrinking the image
#for enlargement:cv.INTER_LINEAR or cv.INTER_CUBIC
#cubic is slow but a lot better in quality
resized = cv.resize(img, (500,500))
cv.imshow("resized", resized)


#cropping
cropped = img[50:200, 200:400]
cv.imshow("cropped", cropped)






cv.waitKey(0)