import cv2
import datetime as dt

#cap=cv2.VideoCapture("D:\\screen.avi")
cap=cv2.VideoCapture(0)
print("For Width==",cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("For Height==",cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print("For Width==",cap.get(3)) # Here 3 for Width, we can use of CAP_PROP_FRAME_WIDTH
print("For Height==",cap.get(4)) # Here 4 for Height

while cap.isOpened():
    ret,frame=cap.read()
    if ret==True:
        font=cv2.FONT_HERSHEY_COMPLEX_SMALL
        text="Height: "+str(cap.get(3))+ " Width: "+ str(cap.get(4))
        Date_data="Date: "+ str(dt.datetime.now())
        frame=cv2.putText(frame,text,(100,100),font,1,(32,50,46),2,cv2.LINE_AA)
        frame=cv2.putText(frame,Date_data,(100,130),font,1,(32,50,46),2,cv2.LINE_AA)
        cv2.imshow("Video",frame)
        if cv2.waitKey(25)==ord("q"):
            break
cap.release()
cv2.destroyAllWindows()