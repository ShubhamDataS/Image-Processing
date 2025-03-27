import cv2
img=cv2.imread("/Users/sankalp/Documents/a.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face=cv2.CascadeClassifier("/Users/sankalp/Documents/haarcascade_frontalface_default.xml")
eye=cv2.CascadeClassifier("/Users/sankalp/Documents/haarcascade_eye.xml")
faces=face.detectMultiScale(gray,1.3,2)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255),2)
    #roi_gray=gray[y:y+h,x:x+w]
    #roi_color=img[y:y+h,x:x+w]
    eyes=eye.detectMultiScale(gray,3,1)
    for (ex,ey,ew,eh) in eyes:
        #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
        cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)

cv2.imshow("detect face", img)
cv2.waitKey(0)
cv2.destroyAllWindows()