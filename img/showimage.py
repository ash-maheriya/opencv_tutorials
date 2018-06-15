import numpy as np
import cv2 as cv

img = cv.imread('messi5.jpg', 0)
cv.imshow('Image Window', img)
k = cv.waitKey(0)
if k == 27:
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite('messigray.png', img)
    cv.destroyAllWindows()
