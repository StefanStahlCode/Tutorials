import cv2 as cv



#good practise to downscale images and video inputs to not be bigger than needed

#take a frame and rescale it to a given value, default 75%
#works for images, videos and live video
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


#changing resolution of a live video
def changeRes(width, height):
    capture.set(3, height)
    capture.set(4, width)



capture = cv.VideoCapture("Videos/dog.mp4")
live = cv.VideoCapture(0)


while True:
    #isTrue, frame = capture.read()

    #frame_resized = rescaleFrame(frame, 0.2)

    isTrue, livefeed = live.read()
    #live_resized = rescaleFrame(livefeed, 0.2)
    cv.imshow("live feed", livefeed)


    #cv.imshow("Video", frame)
    #cv.imshow("Video resized", frame_resized)

    if cv.waitKey(20) & 0xFF==ord("d"):
        break

capture.release()
cv.destroyAllWindows()