# ---------------------------------------------------------------------------- #
#                              Code to Read Image                              #
# ---------------------------------------------------------------------------- #

import cv2 

# Read the image
testImage = cv2.imread("test2.png")

# Check if the image is loaded successfully
if testImage is None:
    print("Error: Image file not found!")
else:
    # Display the image
    cv2.imshow("my image", testImage)
    
    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# ------------------------------------ END ----------------------------------- #
