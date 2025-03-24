import cv2
import numpy as np
#img=cv2.imread("C:\\Users\\AK\\Downloads\\Telegram Desktop\\WhatsApp Image 2025-03-05 at 8.36.48 AM.jpeg",1)
#img=cv2.resize(img,(600,550))

#img=np.zeros([512,512,3],np.uint8)*255 # for black image

img=np.ones([512,512,3],np.uint8)*255 # for whitw image

# Here line accept 5 parameter (img,starting,ending, color, thickness)
img= cv2.line(img,(0,0),(200,100),(124,54,234),5)
img= cv2.arrowedLine(img,(10,20),(200,200),(31,54,234),5)  # color format BGR
img= cv2.rectangle(img,(10,20),(200,200),(31,5,155),5)

# Cirlce- accept (img,starting point, radius, color, thickness)
img= cv2.circle(img,(350,150),(50),(128,54,234),5)

font=cv2.FONT_ITALIC

# Put text- accept (img,Text,starting point, font,font size, color, thickness,line Type)
img=cv2.putText(img,"Shubham",(80,500),font,2,(31,54,234),3,cv2.LINE_AA )

 # Eclipse accept (img,Text,starting point, (lenght,height), ellipse angle, color, thickness)
img= cv2.ellipse(img,(450,230),(100,50),0,0,360,155,5) # 0,0 are rotation point at x,y
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
