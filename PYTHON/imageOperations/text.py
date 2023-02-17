import cv2
import numpy as np

img = cv2.imread('image.png',1)
cv2.imshow('original',img)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'python',(260,364),font,1,(255,255,255),5,cv2.LINE_AA)
cv2.imshow('with text',img)
cv2.waitKey(0)
cv2.distroyAllWindow()