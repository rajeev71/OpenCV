import cv2

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

print(img.shape)
print(img.size)
print(img.dtype)

'Now we want to put football at other place '

b, g, r = cv2.split(img)
img =cv2.merge((b, g, r))

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball


' In order to add two image their dimension should be same so resize it first then add it '

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

# new_img = cv2.add(img, img2)

'If you want to give priority to image then use addweighted()'

new_img = cv2.addWeighted(img, 0.5, img2, 0.5, 0)

cv2.imshow('Image', new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()


