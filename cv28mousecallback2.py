import cv2
import numpy as np

"""
flag=False
ix=0
iy=0
def draw(event,x,y,flag,param):
    global ix,iy
    if event==1:
        
        ix=x
        iy=y    
     
    elif event==4:
        fx=x
        fy=y
        crop=img[iy:fy,ix:fx]
        cv2.imshow("image",crop)

cv2.namedWindow("Drawing")
cv2.setMouseCallback("Drawing",draw)
img= cv2.imread("/Users/sankalp/Documents/a.jpg")
while True:
    cv2.imshow("Drawing",img)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
"""


ix=0
iy=0
def draw(event,x,y,flag,param):
    global ix,iy
    if event==1:
        
        ix=x
        iy=y    
     
    elif event==4:
        fx=x
        fy=y
        crop=frame[iy:fy,ix:fx]
        cv2.imshow("image",crop)
        cv2.imwrite("babu.png",crop)

cv2.namedWindow("Drawing")
cv2.setMouseCallback("Drawing",draw)
cap= cv2.VideoCapture(0)
while cap.isOpened:
    ret,frame=cap.read()
    if ret==True:
        cv2.resize(frame,(600,400))
        cv2.imshow("Drawing",frame)
        if cv2.waitKey(1)==27:
            break
cap.release()
cv2.destroyAllWindows()