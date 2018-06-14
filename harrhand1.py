import cv2
import numpy as np 
import freenect
def get_video():
    array,_ = freenect.sync_get_video()
    array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    return array
 
#cap = cv2.VideoCapture(0)

hand_cascade = cv2.CascadeClassifier('hand.xml')
while(True):
    #ret, frame = cap.read()
    frame = get_video()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hands = hand_cascade.detectMultiScale(gray, 1.1, 5)
    for(x,y,w,h) in hands:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
