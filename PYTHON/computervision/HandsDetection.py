import cv2
import cvzone
#from cvzone.HandTrackingModule import HandDetector
detector=HandDetector(detectionCon=0.8)
cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
while True:
    success,img = cap.read()
    img=detector.findHands(img)
    imList,bboxInfo=detector.findPosition(img)
    print(imList)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
