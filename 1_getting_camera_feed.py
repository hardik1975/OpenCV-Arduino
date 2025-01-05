# ---------------------------------------------------------------------------- #
#                              Getting Camera Feed                             #
# ---------------------------------------------------------------------------- #

import cv2 

# Open webcam
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 500)

# Infinite loop to capture frames
while True:
    # Capture frame-by-frame
    success, frame = cam.read()
    
    if not success:
        print("Error: Failed to capture image from webcam.")
        break
    
    # Display the frame
    cv2.imshow("capture image", frame)
    
    # Exit loop when 'ESC' key is pressed
    if cv2.waitKey(1) & 0xFF == 27:  # 27 is the ASCII code for the ESC key
        print("Exiting...")
        break

# Release resources
cam.release()
cv2.destroyAllWindows()

# ------------------------------------ END ----------------------------------- #
