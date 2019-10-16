import cv2
from matplotlib import pyplot as plt

# Canny Edge detection algorithm composed of 5 steps
# Noise reduction , Gradient Calculation , Non Maximum Suppression , Double threshold , Edge tracking by hyeresis

img = cv2.imread('lena.jpg', 0)

# Canny Edge Detection

cany = cv2.Canny(img, 100, 200)

titles = ['Image', 'Cany']
images = [img, cany]

for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()