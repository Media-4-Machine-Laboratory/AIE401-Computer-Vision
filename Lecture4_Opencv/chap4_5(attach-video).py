# AIE401 - ComputerVision | Attach Video (from webcam)

import cv2 as cv
import numpy as np
import sys

cap = cv.VideoCapture(0)

if not cap.isOpened():
    sys.exit('Camera connection Failed')

frames = []
while True:
    ret, frame = cap.read()

    if not ret:
        print('Failed to acquire frame')
        break

    cv.imshow('video display', frame)

    key = cv.waitKey(1)
    if key==ord('c'):
        frames.append(frame)

    elif key==ord('q'):
        break

cap.release()
cv.destroyAllWindows()

if len(frames)>0:
    imgs = frames[0]
    for i in range(1, min(3, len(frames))):
        imgs =np.hstack((imgs, frames[i]))

    cv.imshow('collected imges', imgs)

    cv.waitKey()
    cv.destroyAllWindows()

print(len(frames))
print(frames[0].shape)
print(type(imgs))
print(imgs.shape)