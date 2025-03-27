import cv2
import numpy as np
ix, iy, fx, fy = -1, -1, -1, -1
drawing = False  # True when the user is selecting a region
selected = False  # True once the region is selected

# Mouse callback function
def select_roi(event, x, y, flags, param):
    global ix, iy, fx, fy, drawing, selected

    if event == cv2.EVENT_LBUTTONDOWN:  # Left mouse button pressed
        ix, iy = x, y
        drawing = True
        selected = False  # Reset selection

    elif event == cv2.EVENT_MOUSEMOVE:  # Mouse movement
        if drawing:
            fx, fy = x, y  # Update final x, y

    elif event == cv2.EVENT_LBUTTONUP:  # Left mouse button released
        fx, fy = x, y
        drawing = False
        selected = True  # Mark selection complete

# Open webcam
cap = cv2.VideoCapture(0)
cv2.namedWindow("Video")
cv2.setMouseCallback("Video", select_roi)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally (mirror effect)
    frame = cv2.flip(frame, 1)

    if drawing:  # Show rectangle while drawing
        temp_frame = frame.copy()
        cv2.rectangle(temp_frame, (ix, iy), (fx, fy), (0, 255, 0), 2)
        cv2.imshow("Video", temp_frame)

    elif selected:  # Zoom into selected region
        # Ensure correct coordinates (handle drag direction)
        x1, x2 = min(ix, fx), max(ix, fx)
        y1, y2 = min(iy, fy), max(iy, fy)

        # Avoid too small regions
        if x2 - x1 > 10 and y2 - y1 > 10:
            cropped = frame[y1:y2, x1:x2]  # Crop selected area
            print(frame.shape)
            zoomed = cv2.resize(cropped, (frame.shape[1], frame.shape[0]), interpolation=cv2.INTER_LINEAR)
            cv2.imshow("Video", zoomed)
        else:
            selected = False  # Reset if selection is too small

    else:
        cv2.imshow("Video", frame)  # Show normal video if no selection

    # Exit on 'Esc' key
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()