import cv2
import numpy as np
img = cv2.imread('image.png',1)
cv2.imshow('original',img)
img = cv2.rectangle(img,(117,126),(390,390),(123,234,56),1)
# img = cv2.rectangle(img,(117,126),(390,390),(123,234,56),-1) -1 for fill the regtangle 

cv2.imshow('regtangle',img)
cv2.waitKey(0)
cv2.distroyAllWindow()