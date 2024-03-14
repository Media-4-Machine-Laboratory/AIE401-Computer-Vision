# AIE401 - ComputerVision | Insert figures & Write

import cv2 as cv
import sys

img = cv.imread('IMG_NAME.extension')

if img is None:
    sys.exit('file Not Found')

cv.rectangle(img, (29, 78), (62, 95), (0, 0, 255), 2)
cv.putText(img, 'text', (29, 77), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

cv.imshow('Draw', img)

cv.waitKey()
cv.destroyAllWindows()