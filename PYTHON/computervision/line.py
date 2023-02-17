import cv2

img = cv2.imread("myimg.jpg",1)

cv2.line(img,(156,154),(347,160),(232, 26, 12),1)

# show the edited img
cv2.imshow("potrait",img)



cv2.waitKey(0)
cv2.distroyAllWindows()