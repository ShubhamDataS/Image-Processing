import cv2 
img=cv2.imread("C:\\Users\\AK\\Downloads\\WhatsApp Image 2024-06-26 at 8.19.14 AM.jpeg",1)
img=cv2.resize(img,(600,800))
# ROI:

"""

#273,322  330,385
#y differeces=63, x=57
roi=img[322:385,273:330]  #[y1:y2,x1:x2]
img[322:385,323:380]=roi
img[322:385,373:430]=roi
img[322:385,223:280]=roi
img[322:385,173:230]=roi
cv2.imwrite("D:\\ROI.jpg",img)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

# split function

"""
b,g,r=cv2.split(img)
cv2.imshow("Original",img)
cv2.imshow("Blue",b)
cv2.imshow("Green",g)
cv2.imshow("Red",r)
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
 
"""   

# Merge function

b,g,r=cv2.split(img)
rgb=cv2.merge([r,g,b])
gbr=cv2.merge([g,b,r])
bgr=cv2.merge([b,g,r])
brg=cv2.merge([b,r,g])
cv2.imshow("Original",img)
cv2.imshow("RGB",rgb)
cv2.imshow("gbr",gbr)
cv2.imshow("bgr",bgr)
cv2.imshow("brg",brg)

k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()



# Creatigng image Border

"""

# Border parameter: img,top,left,right,left,border type,valuecolor
border=cv2.copyMakeBorder(img,10,10,15,15,cv2.BORDER_CONSTANT,value=[0,113,162])
cv2.imshow("Borde Maker",border)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""


# Image blending

"""

img1=cv2.imread("C:\\Users\\AK\\Downloads\\Telegram Desktop\\WhatsApp Image 2025-03-05 at 8.36.48 AM.jpeg",1)
img1=cv2.resize(img1,(600,800))

# Cv2.add 
result1=cv2.add(img,img1)
cv2.imshow("Result1",result1)

# cv2.addWeighted(image,wt,img2,wt,gamma_Value)
result2=cv2.addWeighted(img,0.6,img1,0.4,0)  # gamma_value is for Saturation in image
cv2.imshow("Result2",result2)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
