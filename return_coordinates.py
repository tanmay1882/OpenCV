import cv2
import numpy as np

def getContours(img):
    contours, Hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        if cv2.contourArea(cnt) > 500:
            x, y, w, h = cv2.boundingRect(cv2.approxPolyDP(cnt,0.025*cv2.arcLength(cnt,True),True))
            return [x,y]
        
cam = cv2.VideoCapture(0)

while(True):
    _, frame = cam.read()
    frame = cv2.flip(frame,1)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower = np.array([63,51,26])
    upper = np.array([90,255,150])
    mask = cv2.inRange(hsv,lower,upper)
    c = getContours(mask)
    print(c)
    cv2.imshow("feed",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break