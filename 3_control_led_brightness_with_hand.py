
# ---------------------------------------------------------------------------- #
#                       Control Led Brightness with hand                       #
# ---------------------------------------------------------------------------- #
import cv2 
import mediapipe as mp
import pyfirmata2
import time 
import math

board = pyfirmata2.ArduinoNano("COM3")

# board = pyfirmata2.
ledPin = board.get_pin("d:3:p")

# Open webcam
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 500) 

mp_drawings = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hand = mp_hands.Hands(max_num_hands=1)

# Infinite loop to capture frames
while True:
    # ledPin.write(1) 
    # Capture frame-by-frame
    success, frame = cam.read() 
    
    if not success:
        print("Error: Failed to capture image from webcam.")
        break
    
    # Display the frame
    RGB_Frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hand.process(RGB_Frame)

    if result.multi_hand_landmarks:
        handLandmarks = result.multi_hand_landmarks[0]
        thumpTip = handLandmarks.landmark[4]
        # print(thumpTip)
        indexTip = handLandmarks.landmark[8]
        # print(indexTip)
        distance = math.sqrt((thumpTip.x - indexTip.x)**2 + (thumpTip.y - indexTip.y)**2)
        print(distance)
        ledPin.write(distance) 
        # time.sleep(1)

        # ~~~ Slow ho rha tha esliye comment kr diya ~~~
        # for hand_landmarks in result.multi_hand_landmarks:
        #     print(hand_landmarks)
        #     mp_drawings.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("capture image", frame)
    
    # Exit loop when 'ESC' key is pressed
    if cv2.waitKey(1) & 0xFF == 27:  # 27 is the ASCII code for the ESC key
        print("Exiting...")
        break

# Release resources
cam.release()
cv2.destroyAllWindows()

# ------------------------------------ END ----------------------------------- #
