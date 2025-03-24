import cv2
import numpy as np

# image 1
img=cv2.imread("C:\\Users\\AK\\Downloads\\WhatsApp Image 2024-06-26 at 8.19.14 AM.jpeg",1)
img=cv2.resize(img,(600,800))

# Image 2
img1=cv2.imread("C:\\Users\\AK\\Downloads\\Telegram Desktop\\WhatsApp Image 2025-03-05 at 8.36.48 AM.jpeg",1)
img1=cv2.resize(img1,(600,800))

def blend(x):
    pass

screen=np.zeros([512,512,3],np.uint8)
# Creating Named Window
cv2.namedWindow("Trackbar")
switch="0: OFF \n 1: ON"
cv2.createTrackbar(switch,"Trackbar",0,1,blend)
cv2.createTrackbar("Alpha","Trackbar",1,100,blend)

while True:
    s=cv2.getTrackbarPos(switch,"Trackbar")
    alpha=cv2.getTrackbarPos("Alpha","Trackbar")
    n=alpha/100
    if s==0:
        dst=screen # or screen[:]
    else:
        dst=cv2.addWeighted(img,n,img1,1-n,0)
        cv2.putText(dst,str(alpha),(10,30),cv2.FONT_HERSHEY_TRIPLEX,1,(0,113,65),2)
    cv2.imshow("Blended Image",dst)
    
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()