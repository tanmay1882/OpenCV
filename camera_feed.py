import cv2

cam = cv2.VideoCapture(0)

while(True):
    success, frame = cam.read()
    cv2.imshow("Feed", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break