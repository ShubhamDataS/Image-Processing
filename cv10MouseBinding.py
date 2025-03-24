import cv2
import numpy as np

#  This code is used to find the co-ordinate and color of pixel in image

def mouse_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x," ",y)
        font=cv2.FONT_HERSHEY_PLAIN
        text="."+str(x)+","+str(y)
        cv2.putText(img,text,(x,y),font,1,(123,45,87),2,cv2.LINE_AA)
    if event==cv2.EVENT_RBUTTONDOWN:
        b=img[y,x,0] # 0 for blue
        g=img[y,x,1] #1 for green
        r=img[y,x,2] #2 for red
        font=cv2.FONT_HERSHEY_PLAIN
        bgr_cord="."+str(b)+"."+str(g)+"."+str(r)
        cv2.putText(img,bgr_cord,(x,y),font,1,(43,24,76),2,cv2.LINE_AA)

cv2.namedWindow("Res")
# img=np.ones([512,512,3],np.uint8)*255
img=cv2.imread("C:\\Users\\AK\\Downloads\\Telegram Desktop\\WhatsApp Image 2025-03-05 at 8.36.48 AM.jpeg",1)
img=cv2.resize(img,(800,750))
cv2.setMouseCallback("Res",mouse_event)
while True:
    cv2.imshow("Res",img)
    if cv2.waitKey(1)==27: # 27 is ASCII for ESC
        cv2.imwrite("D:\\draw.jpg",img)
        break
cv2.destroyAllWindows()



# Below code are used to draw circle and rectangle using mouse keys

"""
def draw(event,x,y,flags,param):
    print("x==",x)
    print("y==",y)
    print("flags==",flags)
    print("param==",param)
    if event==cv2.EVENT_FLAG_RBUTTON:
        cv2.circle(img,(x,y),80,(125,0,32),3)
    if event==cv2.EVENT_FLAG_LBUTTON:
        cv2.rectangle(img,(x,y),(x+100,y+50),(25,0,32),3)
cv2.namedWindow("Res")
img=np.ones([512,512,3],np.uint8)*255
cv2.setMouseCallback("Res",draw)
while True:
    cv2.imshow("Res",img)
    if cv2.waitKey(1)==27: # 27 is ASCII for ESC
        cv2.imwrite("D:\\draw.jpg",img)
        break
cv2.destroyAllWindows()
"""