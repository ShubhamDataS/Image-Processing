import cv2

# Video capturing using mobile camera
"""
camera="http://100.91.126.150:8080/video"

cap=cv2.VideoCapture(0)

# connect your laptop and android device with same network either wifi or hotspot
cap.open(camera) # using android camera

#DIVX, XVID, MJPG, X264, WMV1, WMV2
fourcc=cv2.VideoWriter_fourcc(*"XVID")  # XVID is recommended

# it contain 4 parameter ,name,codec,fps,resolution
output=cv2.VideoWriter("D:\\Outputvide.mp4",fourcc,20.0,(640,480))

print(cap)

while cap.isOpened():
    ret,frame=cap.read()
    if ret==True:
        frame=cv2.resize(frame,(700,450))
        cv2.imshow("Videobb",frame)
        output.write(frame)
        if cv2.waitKey(1)==ord("q"): # 0 is for image and 1 is for dynamic
            break
cap.release()
output.release()
cv2.destroyAllWindows()

"""


# Now playing video from youtube
import pafy

url= "https://www.youtube.com/watch?v=SHU2JduotnQ"
data=pafy.new(url)
data= data.getbest(preftype= "mp4")
cap=cv2.VideoCapture(0)

cap.open(data.url) 



print(cap)

while cap.isOpened():
    ret,frame=cap.read()
    if ret==True:
        #frame=cv2.resize(frame,(700,450))
        cv2.imshow("Videobb",frame)
        #output.write(frame)
        if cv2.waitKey(1)==ord("q"): # 0 is for image and 1 is for dynamic
            break
cap.release()
#output.release()
cv2.destroyAllWindows()