import cv2 as cv
import numpy as np

#https://pyimagesearch.com/2021/04/12/opencv-haar-cascades/
#https://github.com/opencv/opencv/tree/master/data/haarcascades
#face detection checks if a face is in the image, face recognition tries to see who the face belongs to
#opencv has pre trained classifier for face detection, most notably haar cascades and local binary patterns (more advanced)
#haar cascades are easy to use, but sensitive to noise
img = cv.imread("Photos/group 1.jpg")
#cv.imshow("Person", img)

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grey Person", grey)

#storing classifier
haar_cascade = cv.CascadeClassifier("face_haar.xml")

#returns a list containing coordinates of found faces
#haar cascades are sensitive to noise
#minNeighbors can be used to adjust this a bit
#comparison:
#face_rect = haar_cascade.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=3) #result in 7 for group 2; result in 14 for group 1
#face_rect = haar_cascade.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=6) #result in 6 for group 2; result in 6 for group 1
#face_rect = haar_cascade.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=12) #result in 2 for group 2; result in 7 for group 1
face_rect = haar_cascade.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=1) # result in 19 for group 1
print(f"Number of faces found = {len(face_rect)}")

#drawing rectangle over detected faces
for (x,y,w,h) in face_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow("Detected faces", img)




cv.waitKey(0)