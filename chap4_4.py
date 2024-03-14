# AIE401 - ComputerVision | Webcam

import cv2 as cv
import sys

#if Windows
#cap=cv.VideoCapture(0, cv.CAP_DSHOW)

#if not Windows
cap = cv.VideoCapture(0)

if not cap.isOpened():
    sys.exit('Camera connection failed')

while True:
    ret, frame = cap.read()

    if not ret:
        print('Failed to acquire frame')
        break
    
    cv.imshow('Video display', frame)

    key=cv.waitKey(1)
    if key==ord('q'):
        break

cap.release()
cv.destroyAllWindows()