import cv2 as cv

#cv.VideoCapture(0) opens webcam, 1 first camera connected to pc, etc
capture = cv.VideoCapture("Videos/dog.mp4")

#while to loop to read video frame by frame
#error  -215:assertion failed -> opencv could not find media file at specified location, here video ends no more frames after last
#alternatively anything that causes opencv to not be able to read image/frame
while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    #if letter d is pressed: stop video
    if cv.waitKey(20) & 0xFF==ord("d"):
        break

capture.release()
cv.destroyAllWindows()
