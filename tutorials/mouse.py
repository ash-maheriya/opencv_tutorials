import numpy as np
import cv2 as cv

db = 76
dg = 142
dr = 0

# mouse callback function
def draw_circle(event, x, y, flags, param):
    global db, dg, dr
#    if event == cv.EVENT_LBUTTONUP:
    cb = np.random.randint(0, 10)
    cg = np.random.randint(0, 10)
    cr = np.random.randint(0, 10)
    db = (db + cb)%360   
    dg = (dg + 1)%360   
    dr = (dr + 1)%360   
    b = np.abs(np.sin(db * np.pi/180)*256)
    g = np.abs(np.sin(-1 * dg * np.pi/180)*256)
    r = np.abs(np.sin(dr * np.pi/180)*256)
    cv.circle(img, (x,y), 100, (b, g, r), 2)

# create a black image, a window and bind the function to window
img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)

while (1):
    cv.imshow('image', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()
