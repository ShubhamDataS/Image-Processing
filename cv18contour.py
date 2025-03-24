import cv2 
import numpy as np
image=cv2.imread(r"C:\Users\AK\Downloads\shapes.png")
img=image.copy()
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,th=cv2.threshold(img_gray,200,255,cv2.THRESH_BINARY_INV)

# contour retrieval: Parameter(image, contour retreival_mode, method )
cont,hierarchy=cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# draw contour on images 
# dra contour parameter=(image,list of contour, no. of contour, color, thickness)

#res=cv2.drawContours(img,cont,-1,(112,0,25),4)  # -1 is for drawing contour over all images 

# moment: it contains information by which can find out center, area, perimeter etc. of a shapes
area=[]
for c in cont:
    m=cv2.moments(c)
    print("Momemnt=",m)
    cx=int(m["m10"]/m["m00"])
    cy=int(m["m01"]/m["m00"])

    # finding area of contour
    a=cv2.contourArea(c)
    area.append(a)

    # Approximation of contour : It is use to approximate the shape with less no. of vertices
    epsilon=0.01*cv2.arcLength(c,True)   # arc lenght take contour and return it 
    data=cv2.approxPolyDP(c,epsilon,True)

    # convexhull is used to provide proper contours convexity
    hull=cv2.convexHull(data)
    
    res=cv2.drawContours(img,[c],-1,(112,0,25),4)
    # res=cv2.drawContours(img,[hull],-1,(112,0,25),4) # it will draw contour convexity
    x,y,w,h=cv2.boundingRect(hull)
    res=cv2.rectangle(res,(x,y),(x+w,y+h),(0,35,255),2)
    res=cv2.circle(res,(cx,cy),7,(0,45,123),-1)
    res=cv2.putText(res,"center",(cx-20,cy-10),cv2.FONT_HERSHEY_PLAIN,1,(0,45,123),2)

# contour Area, Approximation and convex Hull:
    
cv2.imshow("Original",image)
cv2.imshow("threshold",th)
cv2.imshow("Result",res)
cv2.waitKey(0)
cv2.destroyAllWindows()