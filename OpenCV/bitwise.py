import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype="uint8")

rectangle = cv.rectangle(blank.copy(), (30,30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

# cv.imshow("Rectangle", rectangle)
# cv.imshow("Circle", circle)


# img = cv.imread("Photos/park.jpg")
# cv.imshow("Park", img)

#bitwise operators: and, or, xor, not

#bitwise AND
#displays an image that shows the overlap between 2 images
bit_and = cv.bitwise_and(rectangle, circle)
cv.imshow("AND", bit_and)

#bitwise OR
#displays an image that shows both the intersecting and non intersecting regions
bit_or = cv.bitwise_or(rectangle, circle)
cv.imshow("OR", bit_or)

#bitwise XOR
#displays not intersecting regions
bit_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("XOR", bit_xor)


#bitwise NOT
#displays regions enither image are active
bit_not = cv.bitwise_not(rectangle, circle)
cv.imshow("NOT", bit_not)



cv.waitKey(0)