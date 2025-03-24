
import cv2
import numpy as np
img1=cv2.imread("C:\\Users\\AK\\Downloads\\WhatsApp Image 2024-06-26 at 8.19.14 AM.jpeg",1)
img1=cv2.resize(img1,(1024,650))
img2=cv2.imread("C:\\Users\\AK\\Downloads\\Telegram Desktop\\WhatsApp Image 2025-03-05 at 8.36.48 AM.jpeg",1)
#img2=cv2.imread("C:\\Users\\AK\\Downloads\\download (1).jpg",1)
img2=cv2.resize(img2,(400,650))


r,c,ch=img2.shape
roi=img1[0:r,0:c]

# Create mask using Threshold

gray_img=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
_,mask1=cv2.threshold(gray_img,175,255,cv2.THRESH_BINARY_INV)
#mask1=cv2.adaptiveThreshold(gray_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,15,2)

# Background remove
mask_inv=cv2.bitwise_not(mask1)

# put mask into ROI
img1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)

img_ext=cv2.bitwise_and(img2,img2,mask=mask1)

res=cv2.add(img_ext,img1_bg)

cv2.imshow("Image1 ",img1)
cv2.imshow("Image2 ",img2)
#cv2.imshow("ROI ",roi)
#cv2.imshow("threshold ",mask1)
#cv2.imshow("MaskeInverse ",mask_inv)
#n  cv2.imshow("Extracted Background ",img1_bg)
cv2.imshow("Extracted Image ",img_ext)

final=img1
final[0:r,0:c]=res
 
cv2.imshow("Final Image ",final)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Below code are through chatgpt
"""

import cv2
import numpy as np

# Read images
img1 = cv2.imread("C:\\Users\\AK\\Downloads\\WhatsApp Image 2024-06-26 at 8.19.14 AM.jpeg", 1)
img1 = cv2.resize(img1, (1024, 650))

img2 = cv2.imread("C:\\Users\\AK\\Downloads\\Telegram Desktop\\WhatsApp Image 2025-03-05 at 8.36.48 AM.jpeg", 1)
img2 = cv2.resize(img2, (300, 650))
r,c,ch=img2.shape

# Convert img2 to HSV
hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

# Define color range for background removal (Adjust these values)
lower_bound = np.array([0, 0, 193])    # Fine-tune values to match your background color
upper_bound = np.array([193, 56, 255])

# Create mask for background
mask = cv2.inRange(hsv, lower_bound, upper_bound)

# Smooth the mask using Gaussian Blur
mask = cv2.GaussianBlur(mask, (5, 5), 0)

# Apply Morphological operations (Refines mask)
kernel = np.ones((5, 5), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)  # Fill small holes
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)   # Remove small noise
mask = cv2.erode(mask, kernel, iterations=1)           # Shrinks remaining background
mask = cv2.dilate(mask, kernel, iterations=1)          # Restores object edges

# Invert mask
mask_inv = cv2.bitwise_not(mask)

# Extract object from img2 (foreground)
img_ext = cv2.bitwise_and(img2, img2, mask=mask_inv)

# Extract background from img1
roi = img1[0:r, 0:c]
img1_bg = cv2.bitwise_and(roi, roi, mask=mask)

# Merge the object into the background
res = cv2.add(img_ext, img1_bg)

# Place result back into img1
final = img1.copy()
final[0:r, 0:c] = res

# Display results
cv2.imshow("Extracted Object", img_ext)
cv2.imshow("Final Merged Image", final)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
