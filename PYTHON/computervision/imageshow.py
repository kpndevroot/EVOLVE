import cv2

# read the image
img = cv2.imread("myimg.jpg",-1)


# show the image in external window
cv2.imshow("potrait",img)



cv2.waitKey(0)
cv2.distroyAllWindows()