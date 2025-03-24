import cv2
img=cv2.imread("C:\\Users\\AK\\Downloads\\Telegram Desktop\\WhatsApp Image 2025-03-05 at 8.36.48 AM.jpeg",1)
img=cv2.resize(img,(800,750))

img=cv2.flip(img,0)
cv2.imshow("Image",img)
k=cv2.waitKey(0) 
if k==ord("s"):
    cv2.imwrite("D:\\output.png",img)
else:
    cv2.destroyAllWindows()