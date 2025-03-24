import cv2
cap=cv2.VideoCapture(0)

#DIVX, XVID, MJPG, X264, WMV1, WMV2
fourcc=cv2.VideoWriter_fourcc(*"XVID")  # XVID is recommended

# it contain 4 parameter ,name,codec,fps,resolution
output=cv2.VideoWriter("D:\\Output.avi",fourcc,20.0,(640,480))

print(cap)

while cap.isOpened():
    ret,frame=cap.read()
    if ret==True:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Video",frame)
        cv2.imshow("gray",gray)
        output.write(frame)
        if cv2.waitKey(1)==ord("q"): # 0 is for image and 1 is for dynamic
            break
cap.release()
output.release()
cv2.destroyAllWindows()