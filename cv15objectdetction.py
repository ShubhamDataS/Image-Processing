import cv2
import numpy as np

cap=cv2.VideoCapture(0)


def nothing(x):
    pass

cv2.namedWindow("Trackbar")

cv2.createTrackbar("Lower_H","Trackbar",0,255,nothing)
cv2.createTrackbar("Lower_S","Trackbar",0,255,nothing)
cv2.createTrackbar("Lower_V","Trackbar",0,255,nothing)

cv2.createTrackbar("Upper_H","Trackbar",255,255,nothing)
cv2.createTrackbar("Upper_S","Trackbar",255,255,nothing)
cv2.createTrackbar("Upper_V","Trackbar",255,255,nothing)

while True:
    _,frame=cap.read()
    frame=cv2.resize(frame,(400,600))
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    l_h=cv2.getTrackbarPos("Lower_H","Trackbar")
    l_s=cv2.getTrackbarPos("Lower_S","Trackbar")
    l_v=cv2.getTrackbarPos("Lower_V","Trackbar")

    u_h=cv2.getTrackbarPos("Upper_H","Trackbar")
    u_s=cv2.getTrackbarPos("Upper_S","Trackbar")
    u_v=cv2.getTrackbarPos("Upper_V","Trackbar")

    lower_value=np.array([l_h,l_s,l_v])
    upper_value=np.array([u_h,u_s,u_v])
    mask=cv2.inRange(hsv,lower_value,upper_value)
    
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("Original Image",frame   )
    cv2.imshow("Mask",mask)
    cv2.imshow("Result",res)
    if cv2.waitKey(1)==27:
        break
cap.release()
cv2.destroyAllWindows()
