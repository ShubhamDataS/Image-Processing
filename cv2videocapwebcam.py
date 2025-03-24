        

# Now Capture video from webcam and save into memory
import cv2
cap=cv2.VideoCapture(0) # here 0 is for webcam and 1 for external camera
while cap.isOpened():
    ret,frame=cap.read()
    if ret==True:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Webcam",frame)
        cv2.imshow("Webcam2",gray)
        if cv2.waitKey(1)==ord("q"):
           break
cap.release()
cv2.distroyAllWindows()

"""

# playing video from local file

cap=cv2.VideoCapture(r"C:\Users\AK\Desktop\Muskan & Shivam ( Ringceremony ( highlite ).mp4")
while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(600,350))
    to convert color video to gray
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Video",frame)
    cv2.imshow("Gray",gray)
    k=cv2.waitKey(1) 
    if k==ord("s"):      #& 0xFF : mask
        break
cap.release()
cv2.destroyAllWindows()
"""

#



