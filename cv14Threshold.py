import cv2 
import numpy as np
img=cv2.imread("C:\\Users\\AK\\Downloads\\WhatsApp Image 2024-06-26 at 8.19.14 AM.jpeg",0) # instead of 0 we can also use cv2.IMREAD_GRAYSCALE
img=cv2.resize(img,(400,600))

# Simple threshold=(image, min pixel, max_pixel,threshold type)

"""
_,th1=cv2.threshold(img,25,255,cv2.THRESH_BINARY)
_,th2=cv2.threshold(img,25,255,cv2.THRESH_TRUNC)
_,th3=cv2.threshold(img,25,255,cv2.THRESH_BINARY_INV)
_,th4=cv2.threshold(img,25,255,cv2.THRESH_TOZERO)
cv2.imshow("original image",img)
cv2.imshow("Threshold_Binary",th1)
cv2.imshow("Threshold_Trunc",th2)
cv2.imshow("Threshold_Binary_INV",th3)
cv2.imshow("Threshold_ToZero",th4)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""

# Adaptive Thresholding : It is use for gray scale image
# We use it  becasue simple thresholding not able to handle different type of Low Luminous Pixels,
# this alforithm calculate the threshold for a small regions of the image. So we get multiple threshold for different regions in same image.

# Adaptive method: It decides how threshold value is calculated.
# cv2.ADAP

#threshold:(imag,pixel_thresh,max_thresh_pixel,style, no. of pixel,contact_mean)


_,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY) # Simple Thresholding
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow("original image",img)
cv2.imshow("Threshold_Binary",th1)
cv2.imshow("Adaptives_Mean",th2)
cv2.imshow("Adaptives_Gaussian",th3)

cv2.waitKey(0)
cv2.destroyAllWindows()