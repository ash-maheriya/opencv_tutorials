import cv2 as cv
import numpy as np

gst =  "nvcamerasrc ! video/x-raw(memory:NVMM), width=(int)1280, height=(int)720, format=(string)I420, framerate=(fraction)120/1 ! nvvidconv flip-method=0 ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink";

cap = cv.VideoCapture(gst)

while (1):
    # Take each frame
    _, frame = cap.read()

    cv.imshow('frame', frame)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
    elif k == ord('s'):
        cv.imwrite("frame_pick.png", frame)
        print("Image has been saved")

cv.destroyAllWindows()
	
