# ---------------------------------------------------------------------------- #
#                                 Hand Tracking                                #
# ---------------------------------------------------------------------------- #
import cv2 
import mediapipe as mp

# Open webcam
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 500) 

mp_drawings = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hand = mp_hands.Hands()

# Infinite loop to capture frames
while True:
    # Capture frame-by-frame
    success, frame = cam.read() 
    
    if not success:
        print("Error: Failed to capture image from webcam.")
        break
    
    # Display the frame
    RGB_Frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hand.process(RGB_Frame)
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            print(hand_landmarks)
            mp_drawings.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("capture image", frame)
    
    # Exit loop when 'ESC' key is pressed
    if cv2.waitKey(1) & 0xFF == 27:  # 27 is the ASCII code for the ESC key
        print("Exiting...")
        break

# Release resources
cam.release()
cv2.destroyAllWindows()

# ------------------------------------ END ----------------------------------- #
