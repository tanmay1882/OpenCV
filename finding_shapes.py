import cv2
import numpy as np

def getContours(img):
    contours, Hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        cv2.drawContours(blank,cnt,-1,(40,100,0),1)
        approx = cv2.approxPolyDP(cnt,0.025*cv2.arcLength(cnt,True),True)
        objCor = len(approx)
        x, y, w, h = cv2.boundingRect(approx)
        cv2.rectangle(imgcp, (x,y), (x+w,y+h), (0,0,255), 1)
        if(len(approx)==3):
            shape = "triangle"
        elif(len(approx)==4):
            shape = "suqare"
        else:
            shape = "circle"
        cv2.putText(imgcp,shape,(x,y),cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,0,255),2)


src = "shapes.png"
img = cv2.imread(src)
imgcp = img
h, w, c = img.shape
blank = np.ones(shape=(h, w, c), dtype=np.uint8)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (7,7), 1)
img = cv2.Canny(img,50,50)
getContours(img)
cv2.imshow("Image", imgcp)
cv2.waitKey(0)