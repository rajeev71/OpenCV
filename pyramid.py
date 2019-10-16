import cv2
from matplotlib import pyplot as plt

# Lapalician pyramid is formed by the difference between that level in gaussian pyramid and expanded version of its
# upper level in gaussian pyramid

img = cv2.imread('lena.jpg')
layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)

# Lapalicaian

layer = gp[5]
cv2.imshow('Upper level Gaussian Pyramid', layer)
lp = [layer]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp[i])
    lapalacian = cv2.subtract(gp[i-1], gaussian_extended)
    cv2.imshow(str(i), lapalacian)

cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

