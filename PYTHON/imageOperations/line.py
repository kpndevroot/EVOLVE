import cv2


img=cv2.imread('image.png',1)
cv2.imshow("with out line",img)
img=cv2.line(img,(0,478),(255,255),(0,0,255),10)
cv2.imshow("line img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()