import cv2 as cv
import numpy as np

gst =  "nvcamerasrc ! video/x-raw(memory:NVMM), width=(int)1280, height=(int)720, format=(string)I420, framerate=(fraction)120/1 ! nvvidconv flip-method=0 ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink";

cap = cv.VideoCapture(gst)

while (1):
    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    # HSV: (349, 88, 63), (348, 68, 99)
##-    # Define range of blue color in HSV
##-    lower_blue = np.array([110, 50, 50])
##-    upper_blue = np.array([130, 255, 255])
    # Define range of blue color in HSV
    lower_blue = np.array([320/2, 150, 150])
    upper_blue = np.array([360/2, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame, frame, mask = mask)

    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()
	
