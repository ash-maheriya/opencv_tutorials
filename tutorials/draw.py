import numpy as np
import cv2 as cv

# Create a black image

r = 0
inc = True
d = 0
while (1):
    img = np.zeros((512, 512, 3), np.uint8)
    #cv.circle(img, (255,255), r, (0, 0, 0), 2)
    r_ = np.abs(np.sin(d*np.pi/180))
    r = int(r_ * 256)
    d+=1
    d = (d%360)
    ##print("r={}, d={}".format(r,d))
#    if r == 255:
#        inc = False
#    elif r == 20:
#        inc = True            
#    if inc:
#        r+=1
#    else:
#        r-=1
    cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
    cv.line(img, (511, 0), (0, 511), (255, 0, 0), 5)
    cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
    cv.rectangle(img, (384, 510-128), (510, 510), (0, 255, 0), 3)
    cv.rectangle(img, (0, 0), (510-384, 128), (0, 255, 0), 3)
    cv.rectangle(img, (0, 510-128), (510-384, 510), (0, 255, 0), 3)
    cv.circle(img, (255,255), r, (0, 0, 255), 2)

    cv.imshow('frames', img)
    k = cv.waitKey(10) & 0xFF
    if k == ord('q'):
        break
cv.destroyAllWindows()
