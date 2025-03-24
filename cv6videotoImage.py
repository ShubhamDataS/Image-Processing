
import cv2

vidcap=cv2.VideoCapture(r"D:\screen.avi")
ret,img=vidcap.read()
count=0
while True:
    if ret==True:
        cv2.imwrite(r"D:\\frames\\img%d.jpg"%count,img)
        #vidcap.set(cv2.CAP_PROP_POS_MSEC,(count**100))
        ret,img=vidcap.read()
        cv2.imshow("Res",img)
        count+=1
        if cv2.waitKey(1)==ord("q"):
            break
            cv2.destroyAllWindows()
vidcap.release()
cv2.destroyAllWindows() 


# below are different code

"""

import cv2
import os

# Open video file
video_path = r"C:\Users\AK\Desktop\Muskan & Shivam ( Ringceremony ( highlite ).mp4"
vidcap = cv2.VideoCapture(video_path)

# Create output directory if it doesn't exist
output_folder = r"D:\\frames"
os.makedirs(output_folder, exist_ok=True)

count = 0
while True:
    ret, img = vidcap.read()  # Read next frame
    if not ret:  # Break if no more frames
        break
    
    # Save frame as an image
    frame_path = os.path.join(output_folder, f"img{count}.jpg")
    cv2.imwrite(frame_path, img)
    
    count += 1
    cv2.imshow("Extracted Frame", img)

    # Press 'q' to stop early
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
vidcap.release()
cv2.destroyAllWindows()

print(f"Saved {count} frames in {output_folder}") """