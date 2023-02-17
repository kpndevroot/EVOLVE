import cv2

img = cv2.imread("myimg.jpg",1)
cv2.imshow("original",img)
cv2.arrowedLine(img,(34,164),(153,166),(232, 26, 12),5)

# show the edited img
cv2.imshow("potrait-with-arrowline",img)



cv2.waitKey(0)
cv2.distroyAllWindows()