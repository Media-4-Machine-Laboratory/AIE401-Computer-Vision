# AIE401 - ComputerVision | Image Read & Display - 2

import cv2 as cv

img = cv.imread('IMG_NAME.extension')

cv.imshow('img Display', img)
print(img[0, 0, 0], img[0, 0, 1], img[0, 0, 2])

cv.waitKey()
cv.destroyAllWindows()