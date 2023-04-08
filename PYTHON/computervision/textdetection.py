import cv2

# Load the image
img = cv2.imread('vision.jpg')
if img is None:
    print('Error: Could not read image')
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to convert the image to black and white
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Find contours of the text
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw rectangles around the text
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), -1)
    

# Show the image with rectangles around the text
cv2.imshow('Text Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
