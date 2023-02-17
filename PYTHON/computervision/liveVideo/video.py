import cv2

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Loop to continuously get the frames from the webcam
while True:
    ret, frame = cap.read()
    
    cv2.imshow('Live Video', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
