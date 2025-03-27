import cv2
img=cv2.imread("/Users/sankalp/Documents/a.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

def nothing(x):
    pass

cv2.namedWindow("Sketch")
cv2.createTrackbar("Scale","Sketch",0,255,nothing)
cv2.createTrackbar("Color","Sketch",0,255,nothing)

while True:
    scale=cv2.getTrackbarPos("Scale","Sketch")
    color=cv2.getTrackbarPos("Color","Sketch")

    inverted_gray=color-gray # or 255-gray
    blur_gray=cv2.GaussianBlur(inverted_gray,(21,21),0)
    inverted_blur=color-blur_gray
    filter=cv2.divide(gray,inverted_blur,scale=scale)
    cv2.imshow("Image",filter)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()