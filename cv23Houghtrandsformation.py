import cv2
import numpy as np

"""
img = cv2.imread('Data\\chess.jpg')
img = cv2.resize(img,(400,400))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,10,200,apertureSize = 3)

#function accept parameter(img,rho,theta)
lines = cv2.HoughLines(edges,1,np.pi/180,200)
#rho value -- distance resolution of pixels
#thetha - angle resolution
#line threshold
for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img,(x1,y1),(x2,y2),(255,0,255),2)

cv2.imshow("edge",edges)
cv2.imshow("lines",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""

#Second Type of Hough Transformation
"""
img = cv2.imread('H:\\Data\\square.png')
img = cv2.resize(img,(400,400))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
cv2.imshow('edges', edges)
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=8,
                        maxLineGap=100)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(100,200,125),2)

cv2.imshow('image', img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()
"""