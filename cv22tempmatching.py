import cv2
import numpy as np

"""
# Target image
img=cv2.imread("/Users/sankalp/Documents/avengers.jpg",1)
gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# template image
img1=cv2.imread("/Users/sankalp/Documents/temp.jpg",0)
h,w=img1.shape

# Matching the template: parameter(image,templte image, method)
res= cv2.matchTemplate(gray_image,img1,cv2.TM_CCORR_NORMED)

#finding brightest pixel
threshold=0.999
loc=np.where(res>threshold)
for i in zip(*loc[::-1]):
    cv2.rectangle(img,i,(i[0]+w,i[1]+h),(0,45,34),2)

cv2.resize(res,(800,600))
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""

# Here we are going to make dynamic threshold

"""

# Target image
img=cv2.imread("/Users/sankalp/Documents/avengers.jpg",1)
gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# template image
img1=cv2.imread("/Users/sankalp/Documents/temp.jpg",0)
h,w=img1.shape

# Matching the template: parameter(image,templte image, method)
res= cv2.matchTemplate(gray_image,img1,cv2.TM_CCORR_NORMED)

#finding brightest pixel
threshold=cv2.minMaxLoc(res) # it will return 4 values 

# getting co-ordinate for threshold
x1= threshold[3]
cv2.rectangle(img,x1,(x1[0]+w,x1[1]+h),(0,45,34),4)

cv2.resize(res,(800,600))
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""

# Using different Methods:-----

# Target image
img=cv2.imread("/Users/sankalp/Documents/avengers.jpg",1)
g_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_image=g_image.copy()

# template image
img1=cv2.imread("/Users/sankalp/Documents/temp.jpg",0)
h,w=img1.shape
methods=['cv2.TM_CCORR_NORMED','cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
         'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
for i in methods:
    print("Method:==",i)
    gray_image=g_image.copy()
    method=eval(i)
# Matching the template: parameter(image,templte image, method)
    res= cv2.matchTemplate(gray_image,img1,method)

    #finding brightest pixel
    threshold=cv2.minMaxLoc(res) # it will return 4 values 

    # getting co-ordinate for threshold
    x1= threshold[3]
    cv2.rectangle(img,x1,(x1[0]+w,x1[1]+h),(0,45,34),4)
    cv2.resize(img,(300,400))
    cv2.imshow(i+"Image",img)


cv2.waitKey(0)
cv2.destroyAllWindows()