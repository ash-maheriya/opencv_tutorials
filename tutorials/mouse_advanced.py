import numpy as np
import cv2 as cv
drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
color = True # if True, use green. Press 'c' to toggle to red
ix,iy = -1,-1

img = np.zeros((512,512,3), np.uint8)
oimg = np.zeros((512,512,3), np.uint8)

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    global ox, oy
    global img
    global oimg
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
        oimg[:] = img 
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                img[:] = oimg
                cv.rectangle(img,(ix,iy),(x,y),(0, 0, 255), 1)
            else:
                cv.circle(img,(x,y),5,(0,0,255),-1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            img[:] = oimg
            if color == True:
                cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv.rectangle(img,(ix,iy),(x,y),(255,0,0),-1)
        else:
            cv.circle(img,(x,y),5,(0,0,255),-1)

cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == ord('c'):
        color = not color
    elif k == 27:
        break
cv.destroyAllWindows()

