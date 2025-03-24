import cv2
import pyautogui as p
import numpy as np

# creating resolution
rs=p.size()  # it will capture the size of the my screen
fps=20.0

fourcc=cv2.VideoWriter_fourcc(*'XVID')
output=cv2.VideoWriter("D:\\Screen.avi",fourcc,fps,rs)

# Create recording module
cv2.namedWindow("Live Recording",cv2.WINDOW_NORMAL)
#cv2.resizeWindow("Live Recording",(800,600))   OR
cv2.setWindowProperty("Live Recording", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    img=p.screenshot()
    f=np.array(img)
    f=cv2.cvtColor(f,cv2.COLOR_BGR2RGB)
    #display_frame = cv2.resize(f, (800, 600))
    output.write(f)
    cv2.imshow("Live Recording",f)
    if cv2.waitKey(1)& 0xFF==ord("q"):
        break
output.release()
cv2.destroyAllWindows()
