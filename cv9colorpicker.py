import cv2
import numpy as np 

def cross(x):
    pass
# create blank image and name window
img=np.zeros([512,512,3],np.uint8)
cv2.namedWindow("Color Picker")

# Creating Tracker
cv2.createTrackbar("0: OFF \n 1: ON","Color Picker",0,1,cross)
cv2.createTrackbar("B","Color Picker",0,255,cross)
cv2.createTrackbar("G","Color Picker",0,255,cross)
cv2.createTrackbar("R","Color Picker",0,255,cross)

while True:
    cv2.imshow("Color Picker",img)
    if cv2.waitKey(1)==27:
        break
    s=cv2.getTrackbarPos("0: OFF \n 1: ON","Color Picker")
    b=cv2.getTrackbarPos("B","Color Picker")
    g=cv2.getTrackbarPos("G","Color Picker")
    r=cv2.getTrackbarPos("R","Color Picker")
    if s==0:
        img[:]=0
    else:
        img[:]=[b,g,r]
cv2.destroyAllWindows()


