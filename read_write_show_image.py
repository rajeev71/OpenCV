import cv2

''' imread(imagename , flagvalue(integervalue 1-color,-1-as it is with alpha chanel,0-grayscale mode)) even if you give wrong imagename it will not give error '''

img = cv2.imread('lena.jpg',1)

'Display Image '

cv2.imshow('Image',img)
k=cv2.waitKey(0)

if k==27:
    cv2.destroyAllWindows()

elif k == ord('s'):

    'Write Image '
    cv2.imwrite('lena_copy.jpg',img)
    cv2.destroyAllWindows()


