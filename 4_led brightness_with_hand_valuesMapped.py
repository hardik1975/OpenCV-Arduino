# ---------------------------------------------------------------------------- #
#               Control Led Brightness with hand (Values Mapped)               #
# ---------------------------------------------------------------------------- #

import cv2 
import mediapipe as mp
import pyfirmata2
import time 
import math

def map_value_positive(input_value, input_min, input_max, output_min, output_max):
    # Map the value to the desired range
    mapped_value = (input_value - input_min) * (output_max - output_min) / (input_max - input_min) + output_min
    # Ensure the output is always positive
    return max(mapped_value, 0)

board = pyfirmata2.ArduinoNano("COM3")

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
    success, frame = cam.read() 
    
    if not success:
        print("Error: Failed to capture image from webcam.")
        break
    
    # Convert the frame to RGB
    RGB_Frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hand.process(RGB_Frame)

    if result.multi_hand_landmarks:
        handLandmarks = result.multi_hand_landmarks[0]
        thumpTip = handLandmarks.landmark[4]
        indexTip = handLandmarks.landmark[8]
        distance = math.sqrt((thumpTip.x - indexTip.x)**2 + (thumpTip.y - indexTip.y)**2)

        # Map distance to PWM range (0.0–1.0)
        mapped_value = map_value_positive(distance, 0.02, 0.5, 0, 1)
        mapped_value = min(1.0, max(0.0, mapped_value))  # Clamp value

        print(f"Distance: {distance}, Mapped Value: {mapped_value}")

        # Write to the PWM pin
        ledPin.write(mapped_value)

    cv2.imshow("Capture Image", frame)
    
    # Exit loop when 'ESC' key is pressed
    if cv2.waitKey(1) & 0xFF == 27:  # 27 is the ASCII code for the ESC key
        print("Exiting...")
        break

# Release resources
cam.release()
cv2.destroyAllWindows()

# ------------------------------------ END ----------------------------------- #
