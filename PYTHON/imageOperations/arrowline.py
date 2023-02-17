import cv2
import numpy as np

img = cv2.imread('image.png',1)
# img = cv2.line(img,(0,0),(255,255),(0,0,255),10)
img= cv2.arrowedLine(img,(0,255),(255,255),(93,120,255),10)
cv2.imshow('drawline',img)
cv2.waitKey(0)
cv2.distroyAllWindows()