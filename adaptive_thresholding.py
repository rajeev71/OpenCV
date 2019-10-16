import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('gradient.png')

_, th2 = cv.threshold(img, 50, 255, cv.THRESH_BINARY_INV) # If pixel is less than 50 assign to black else white
_, th3 = cv.threshold(img, 50, 255, cv.THRESH_TRUNC)
_, th4 = cv.threshold(img, 50, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img, 50, 255, cv.THRESH_TOZERO_INV)

# Adaptive Thresholding

# _, th6 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, th2, th3, th4, th5]

for i in range(5):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])


plt.show()
#cv.waitKey(0)
#cv.destroyAllWindows()
