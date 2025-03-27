"""

import cv2
import numpy as np
flags=False
ix=-1
iy=-1
temp_img=None
def draw(event,x,y,flag,param):
    global ix,iy,temp_img,flags,img
    if event==1:
        flags=True
        ix=x
        iy=y
        temp_img=img.copy()
    
    elif event==0:
        if flags==True:        
            temp_img=img.copy()
            cv2.rectangle(temp_img,(ix,iy),(x,y),(255,67,255),2)
    elif event==4:
        flags=False
        cv2.rectangle(temp_img,(ix,iy),(x,y),(255,67,255),2)

cv2.namedWindow("Drawing")
cv2.setMouseCallback("Drawing",draw)
img= np.ones([512,512,3],np.uint8)*255
while True:
    if temp_img is not None:
        cv2.imshow("Drawing",temp_img)
    else: 
        cv2.imshow("Drawing",img)
    if cv2.waitKey(1)& 0xFF==27:
        break
cv2.destroyAllWindows()
"""


"""
import cv2
import numpy as np

# Initialize variables
drawing = False  # True when the user is drawing
ix, iy = -1, -1  # Initial coordinates
temp_img = None  # Temporary image to show dragging effect

# Mouse callback function
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, temp_img, img

    if event == cv2.EVENT_LBUTTONDOWN: # 1 # Mouse press -> Start drawing
        drawing = True
        ix, iy = x, y  # Store the starting point
        temp_img = img.copy()  # Store a copy to draw on

    elif event == cv2.EVENT_MOUSEMOVE: #0 # Mouse moves -> Update rectangle dynamically
        if drawing:
            temp_img = img.copy()  # Reset to original image
            cv2.rectangle(temp_img, (ix, iy), (x, y), (0, 255, 0), 2)  # Draw rectangle

    elif event == cv2.EVENT_LBUTTONUP: # 4 # Mouse release -> Finalize drawing
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)  # Final rectangle on main image

# Create a window and set the mouse callback
cv2.namedWindow("Draw Rectangle")
cv2.setMouseCallback("Draw Rectangle", draw_rectangle)

# Create a blank white image
img = np.ones((500, 700, 3), dtype=np.uint8) * 255

while True:
    if temp_img is not None:
        cv2.imshow("Draw Rectangle", temp_img)  # Show preview while dragging
    else:
        cv2.imshow("Draw Rectangle", img)  # Show final image

    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Press 'Esc' to clear and restart
        img = np.ones((500, 700, 3), dtype=np.uint8) * 255
        temp_img = None  # Reset temp image

    elif key == ord('q'):  # Press 'q' to exit
        break

cv2.destroyAllWindows()
"""


# this code is for erasing the image 

import cv2
import numpy as np

# Initialize variables
drawing = False   # Flag to check if drawing is happening
erasing = False   # Flag to check if erasing is happening
ix, iy = -1, -1   # Initial coordinates
temp_img = None   # Temporary image for live preview

# Create a blank white canvas
img = np.ones((500, 700, 3), dtype=np.uint8) * 255  

# Mouse callback function
def draw_erase(event, x, y, flags, param):
    global ix, iy, drawing, erasing, img, temp_img

    # Left Button Pressed - Start drawing a rectangle
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y  # Store starting coordinates
        temp_img = img.copy()  # Copy the original image for preview

    # Right Button Pressed - Start erasing
    elif event == cv2.EVENT_RBUTTONDOWN:
        erasing = True

    # Mouse Moving
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            temp_img = img.copy()  # Reset to original image
            cv2.rectangle(temp_img, (ix, iy), (x, y), (0, 255, 0), 2)  # Draw a temporary rectangle
        elif erasing:
            cv2.circle(img, (x, y), 20, (255, 255, 255), -1)  # Erase by drawing white circles

    # Left Button Released - Finalize drawing
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)  # Final rectangle
        temp_img = None  # Reset temp image

    # Right Button Released - Stop erasing
    elif event == cv2.EVENT_RBUTTONUP:
        erasing = False

# Create window and set mouse callback
cv2.namedWindow("Draw & Erase")
cv2.setMouseCallback("Draw & Erase", draw_erase)

while True:
    # Show the preview image if drawing, otherwise show the original
    if temp_img is not None:
        cv2.imshow("Draw & Erase", temp_img)  # Show real-time preview
    else:
        cv2.imshow("Draw & Erase", img)  # Show final image

    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Press 'Esc' to reset the canvas
        img = np.ones((500, 700, 3), dtype=np.uint8) * 255
        temp_img = None  # Reset preview
    elif key == ord('q'):  # Press 'q' to exit
        break

cv2.destroyAllWindows()
