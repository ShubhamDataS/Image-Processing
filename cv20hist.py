import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("/Users/sankalp/Documents/thor.jpg")
img1=np.zeros([200,200],np.uint8)

# Histogram of Image
"""
cv2.rectangle(img1,(0,100),(200,200),(255),-1)
cv2.rectangle(img1,(0,50),(80,100),(127),-1)

# it accepts : calchist=([image],[channel],mask,[histsize],range[0-255])
hist=cv2.calcHist([img1],[0],None,[256],[0,256])

plt.plot(hist)
plt.show()

cv2.imshow("Image",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

# Histogram of color Image

"""
b,g,r=cv2.split(img)
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.title("Colorful histogram")
plt.show()

cv2.imshow("Image",img)
cv2.waitKey(0)
"""

# histogram for gray scale

"""
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Image",img)
hist=cv2.calcHist([gray_img],[0],None,[256],[0,256])
plt.plot(hist)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
"""

# Equalize histogram
"""
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
eq=cv2.equalizeHist(gray_img)
res=np.hstack((gray_img,eq))
cv2.imshow("Image",res)
hist=cv2.calcHist([eq],[0],None,[256],[0,256])
plt.plot(hist)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
"""

#CLAHE=(Contrast Limited Adaptive Histogram Equalization)
# it is use to enhance image and handle noise

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
clhe=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
cl1=clhe.apply(gray_img)
cv2.imshow("Image",cl1)
hist=cv2.calcHist([cl1],[0],None,[256],[0,256])
plt.plot(hist)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()