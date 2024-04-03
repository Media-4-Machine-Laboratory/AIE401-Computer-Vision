import skimage
import numpy as np
import cv2 as cv
import time

img = skimage.data.coffee()

start = time.time()

slic = skimage.segmentation.slic(img, compactness=20, n_segments=600)

g = skimage.graph.rag_mean_color(img, slic, mode='similarity') 
ncut = skimage.graph.cut_normalized(slic, g)

print(img.shape,'Coffee image segmentation takes ', time.time()-start, 'sec')

marking=skimage.segmentation.mark_boundaries(img, ncut)
ncut_coffee=np.uint8(marking*255.0)

cv.imshow('Normalized cut',cv.cvtColor(ncut_coffee,cv.COLOR_RGB2BGR))  

cv.waitKey()
cv.destroyAllWindows()