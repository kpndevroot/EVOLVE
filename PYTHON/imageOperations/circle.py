import cv2
import numpy as np

img = cv2.imread('image.png',1)


cv2.imshow('original',img)
img = cv2.circle(img,(414,414),50,(255,255,255),-1)
cv2.imshow('circle',img)
cv2.waitKey(0)
cv2.distroyAllWindow()