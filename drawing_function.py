import cv2
import numpy as np

img = cv2.imread('lena.jpg', 1)

'To draw anything takes five argument 1. variable ,2. Initial cordinate ,3. Final Cordinate , 4. color in BGR format ,5. width'

img = cv2.line(img,(0,0),(255,255),(147,96,44),10)

'To show Text On Image'
'variable name , Text Name , starting coordinate , font , font_size ,color ,thickness ,line type'


font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 10 , cv2.LINE_AA)


cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()