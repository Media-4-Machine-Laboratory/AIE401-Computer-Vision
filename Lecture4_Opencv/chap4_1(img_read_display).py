# AIE401 - ComputerVision | Image Read & Display - 1

import cv2 as cv
import sys

img = cv.imread('IMG_NAME.extension')

if img is None:
    sys.exit('file Not Found')

cv.imshow('img Display', img)

cv.waitKey()
cv.destroyAllWindows()

print(type(img))
print(img.shape)