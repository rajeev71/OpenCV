# Thresholding is a segmentation technique used to separates object from its background  .
# It involves comparing each pixels value of image with predefined threshold value .

import cv2 as cv

img = cv.imread('gradient.png')

ret_value, th = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

cv.imshow('Frame', th)
cv.imshow("Original", img)
cv.waitKey(0)
cv.destroyAllWindows()