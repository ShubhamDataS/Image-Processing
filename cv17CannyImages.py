import cv2
import numpy as np

#img1=cv2.imread("C:\\Users\\AK\\Downloads\\WhatsApp Image 2024-06-26 at 8.19.14 AM.jpeg",1)
img1=cv2.imread("C:\\Users\\AK\\Downloads\\Telegram Desktop\\WhatsApp Image 2025-03-05 at 8.36.48 AM.jpeg",1)
img1=cv2.resize(img1,(400,500))

"""
def nothing(x):
    pass

gray_img=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
cv2.namedWindow("Canny")
cv2.createTrackbar("Thresh1","Canny",0,255,nothing)
cv2.createTrackbar("Thresh2","Canny",0,255,nothing)

while True:
    a=cv2.getTrackbarPos("Thresh1","Canny")
    b=cv2.getTrackbarPos("Thresh2","Canny")
    res=cv2.Canny(gray_img,a,b)
    cv2.imshow("Canny",res)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows
"""

# Pyramid Down

img2=img1.copy()
for i in range(4):
    img2=cv2.pyrDown(img2)
    cv2.imshow("Res"+str(i),img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
