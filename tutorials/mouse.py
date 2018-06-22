import numpy as np
import cv2 as cv

db = 76
dg = 142
dr = 0

def get_random(a, b):
    temp = np.random.random_sample() * (b - a) + a
#    print("a = {}, b = {}, random number = {}".format(a, b, temp))
    return temp

# mouse callback function
def draw_circle(event, x, y, flags, param):
    global db, dg, dr
    cb = get_random(0, 2)
    cg = get_random(3, 7)
    cr = get_random(1, 4)
    db = (db + cb)
    dg = (dg - cg)
    dr = (dr + cr)
    b = np.abs(np.sin(db * np.pi/180)*256)
    g = np.abs(np.sin(dg * np.pi/180)*256)
    r = np.abs(np.sin(dr * np.pi/180)*256)
#    b = int(get_random(0, 256))
#    g = int(get_random(0, 256))
#    r = int(get_random(0, 256))
    cv.circle(img, (x,y), 100, (b, g, r), 2)

# create a black image, a window and bind the function to window
img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)

while (1):
    cv.imshow('image', img)
    if cv.waitKey(2) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()
