import cv2
import numpy as np

# Function to handle mouse events
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Draw a circle with a 2cm radius at the clicked location in yellow (outerline only)
        cv2.circle(img, (x, y), int(1 / 0.0254), (0, 255, 255), 2)
        cv2.imshow('Image', img)

# Create a black image
img = np.zeros((500, 500, 3), dtype=np.uint8)

# Create a window and set the mouse callback function
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', mouse_callback)

# Main loop to display the image and wait for user input
while True:
    cv2.imshow('Image', img)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Press 'Esc' to exit
        break

cv2.destroyAllWindows()