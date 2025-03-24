import cv2
import numpy as np

# Bitwise Operation AND, OR,NOT, XOR

"""
img1=np.zeros([512,512,3],np.uint8)
img1=cv2.rectangle(img1,(10,30),(300,250),(255,255,255),-1)

img2=np.zeros([512,512,3],np.uint8)
img2=cv2.rectangle(img2,(50,150),(200,550),(255,255,255),-1)


cv2.imshow("Image1",img1)
cv2.imshow("Image2",img2)

bit_and=cv2.bitwise_and(img1,img2)
cv2.imshow("AND",bit_and)

bit_or=cv2.bitwise_or(img1,img2)
cv2.imshow("OR",bit_or)

bit_not=cv2.bitwise_not(img1,img2)
cv2.imshow("NOT",bit_not)

bit_xor=cv2.bitwise_xor(img1,img2)
cv2.imshow("XOR",bit_xor)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""

#HSV:- HUE Saturation value
"""
img=cv2.imread("C:\\Users\\AK\\Downloads\\ball-pit-1029865_1920.jpg",1)
img=cv2.resize(img,(400,600))
while True:
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    u_value=np.array([144,255,255])
    l_value=np.array([97,68,106])
    # Creating mask
    mask=cv2.inRange(hsv,l_value,u_value)
    res=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("IMage",img)
    cv2.imshow("Mask",mask)
    cv2.imshow("Result",res)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
"""

# TrACKBAR FOR HSV

#img=cv2.imread("C:\\Users\\AK\\Downloads\\ball-pit-1029865_1920.jpg",1)
img=cv2.imread("C:\\Users\\AK\\Downloads\\Telegram Desktop\\WhatsApp Image 2025-03-05 at 8.36.48 AM.jpeg",1)
img=cv2.resize(img,(400,600))

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
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    l_h=cv2.getTrackbarPos("Lower_H","Trackbar")
    l_s=cv2.getTrackbarPos("Lower_S","Trackbar")
    l_v=cv2.getTrackbarPos("Lower_V","Trackbar")

    u_h=cv2.getTrackbarPos("Upper_H","Trackbar")
    u_s=cv2.getTrackbarPos("Upper_S","Trackbar")
    u_v=cv2.getTrackbarPos("Upper_V","Trackbar")

    lower_value=np.array([l_h,l_s,l_v])
    upper_value=np.array([u_h,u_s,u_v])
    mask=cv2.inRange(hsv,lower_value,upper_value)
    
    res=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("Original Image",img)
    cv2.imshow("Mask",mask)
    cv2.imshow("Result",res)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
