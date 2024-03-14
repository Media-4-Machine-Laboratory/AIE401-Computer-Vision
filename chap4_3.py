# AIE401 - ComputerVision | Conversion & Resize

import cv2 as cv
import sys

img = cv.imread('IMG_NAME.extension')

if img is None:
    sys.exit('img Not Found')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_small = cv.resize(gray, dsize=(0,0), fx=0.5, fy=0.5)

cv.imwrite('IMG_NAME_gray.png', gray)
cv.imwrite('IMG_NAME_small.png', gray_small)

cv.imshow('Color img', img)
cv.imshow('Gray image', gray)
cv.imshow('Gray image small', gray_small)

cv.waitKey()
cv.destroyAllWindows()