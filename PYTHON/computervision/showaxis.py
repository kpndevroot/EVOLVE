import cv2

import matplotlib.pyplot as plt

image= cv2.imread('myimg.jpg')

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()
cv2.waitKey(0)
cv2.distroyAllWindow()
