import cv2

# Load an image
img = cv2.imread('input.png')

# Add text to the image
font = cv2.FONT_HERSHEY_SIMPLEX
text = 'Hello, OpenCV!'
(text_width, text_height), baseline = cv2.getTextSize(text, font, fontScale=1, thickness=1)
text_coord = (img.shape[1] - text_width - 10, img.shape[0] - 10)
cv2.putText(img, text, text_coord, font, fontScale=1, color=(0,0,255), thickness=1)

# Save the image
cv2.imwrite('edited.png', img)
