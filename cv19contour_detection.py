import cv2
import numpy as np 
cap=cv2.VideoCapture(0)
#cap=cv2.resize(cap,(350,400))


def nothing(x):
    pass
cv2.namedWindow("Object Detection")
cv2.resizeWindow("Object Detection",(300,300))
cv2.createTrackbar("Thresh","Object Detection",0,255,nothing)

cv2.createTrackbar("LH","Object Detection",0,255,nothing)
cv2.createTrackbar("LS","Object Detection",0,255,nothing)
cv2.createTrackbar("LV","Object Detection",0,255,nothing)

cv2.createTrackbar("UH","Object Detection",255,255,nothing)
cv2.createTrackbar("US","Object Detection",255,255,nothing)
cv2.createTrackbar("UV","Object Detection",255,255,nothing)

while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(400,400))
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lh=cv2.getTrackbarPos("LH","Object Detection")
    ls=cv2.getTrackbarPos("LS","Object Detection")
    lv=cv2.getTrackbarPos("LV","Object Detection")

    uh=cv2.getTrackbarPos("UH","Object Detection")
    us=cv2.getTrackbarPos("US","Object Detection")
    uv=cv2.getTrackbarPos("UV","Object Detection")

    lower=np.array([lh,ls,lv])
    upper=np.array([uh,us,uv])

    mask=cv2.inRange(hsv,lower,upper)
    filter=cv2.bitwise_and(frame,frame,mask=mask)

    mask1=cv2.bitwise_not(mask)
    thresh=cv2.getTrackbarPos("Thresh","Object Detection")
    _,th=cv2.threshold(mask1,thresh,255,cv2.THRESH_BINARY)

 # performing dilation
    dil=cv2.dilate(th,(1,1),iterations=6)
    cont,hier=cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    

    for c in cont:
        epsilon=0.001*cv2.arcLength(c,True)
        data=cv2.approxPolyDP(c,epsilon,True)
        hull=cv2.convexHull(data)
        cv2.drawContours(frame,cont,-1,(124,255,32),3)
        cv2.drawContours(frame,[hull],-1,(0,255,32),4)


    #           cv2.imshow("mask",mask)
    #cv2.imshow("mask1",mask1)
    cv2.imshow("original",frame)
    cv2.imshow("Threshold",th)
    cv2.imshow("filter",filter)
    if cv2.waitKey(1)==27:
        break
cap.release()
cv2.destroyAllWindows()