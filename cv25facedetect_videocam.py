import cv2

face = cv2.CascadeClassifier("/Users/sankalp/Documents/haarcascade_frontalface_default.xml")

def detector(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(30, 30))
    eye=cv2.CascadeClassifier("/Users/sankalp/Documents/haarcascade_eye.xml")

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)  # Green rectangle
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        eyes=eye.detectMultiScale(roi_gray,1.2,5)
        for (ex,ey,ew,eh) in eyes:
            cv2.circle(roi_color,(ex+20,ey+20),25,(0,0,255),2)
    return frame

# Start video capture
cap=cv2.VideoCapture(0)
while cap.isOpened():
    ret,img=cap.read()
    img=cv2.flip(img,1)
    cv2.imshow("Video",detector(img))
    if cv2.waitKey(1)==27:
        break
cap.release()
cv2.destroyAllWindows()

# Below is code for zooming camera

"""

# Load Haar cascade
face_cascade = cv2.CascadeClassifier("/Users/sankalp/Documents/haarcascade_frontalface_default.xml")

def detector(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)  # Green rectangle
    return frame

# Start video capture
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Get the original frame dimensions
ret, frame = cap.read()
if not ret:
    print("Error: Could not read frame.")
    cap.release()
    exit()

height, width, _ = frame.shape

# Define the cropping area for 2.5x zoom
zoom_factor = 2
new_width = int(width / zoom_factor)
new_height = int(height / zoom_factor)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Exit if frame is not read correctly

    # Define upper center cropping region
    center_x = width // 2
    x1 = max(center_x - new_width // 2, 0)
    x2 = min(center_x + new_width // 2, width)

    # Crop only the **upper part** of the frame
    y1 = 0  # Start from the top
    y2 = min(new_height, height)  # Crop height limited by frame size

    # Extract cropped region and resize back to original size
    cropped_frame = frame[y1:y2, x1:x2]
    zoomed_frame = cv2.resize(cropped_frame, (width, height), interpolation=cv2.INTER_LINEAR)

    # Flip for natural view and detect faces
    zoomed_frame = cv2.flip(zoomed_frame, 1)
    zoomed_frame = detector(zoomed_frame)

    # Show the output
    cv2.imshow("Upper-Center Zoomed Face Detection", zoomed_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit on pressing 'q'
        break

cap.release()
cv2.destroyAllWindows()

"""

