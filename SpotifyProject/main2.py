import cv2 
import time 
import mediapipe as mp
import numpy as np
from spoti import *
import threading

#volume of the playback
volume = 50

def execute_skip_to_next():
    skipToNext()

def execute_skip_to_previous():
    skipToPrevious()

def execute_volume_change():
    changeVolume(volume)

def execute_delay():
    time.sleep(100)

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
myDraw = mp.solutions.drawing_utils

#for calling a function only once in a while loop
function_called = False

while True:
    ret, frame = cap.read()

    if not ret:
        break

    imageRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
    results = hands.process(imageRGB)


    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:
            

            for id, lm in enumerate(hand.landmark):
                

                # setting the center to tip of pointing finger
                if id == 8:
                    

                    #in this case, height = 480, width = 640, channel = 3
                    height, width, channel = frame.shape
                    x_coordinate, y_coordinate = int(lm.x * width), int(lm.y * height)
                    #print(x_coordinate, y_coordinate)

                    #conditions for coordinates to navigate left or right
                    if width > x_coordinate > 450.0  and not function_called:
                        thread = threading.Thread(target=execute_skip_to_previous)
                        thread.start()
                        function_called = True


                    if 0.0 < x_coordinate < 150.0 and not function_called:
                        thread = threading.Thread(target=execute_skip_to_next)
                        thread.start()
                        function_called = True


                    if 380.0 < y_coordinate < height and volume > 0:
                        thread = threading.Thread(target=execute_volume_change)
                        thread.start()
                        volume = volume - 2
                        #print(volume)
                        thread = threading.Thread(target=execute_delay)
                        thread.start()
                        
                    
                    if 0.0 < y_coordinate < 150.0 and volume < 100:
                        thread = threading.Thread(target=execute_volume_change)
                        thread.start()
                        volume = volume + 2
                        #print(volume)
                        thread = threading.Thread(target=execute_delay)
                        thread.start()

                    if 150.0 <= x_coordinate <= 430.0:
                        function_called = False
             
            #cv2.circle(frame,(x_coordinate, y_coordinate), 10, (0, 255 , 0), cv2.FILLED)
      
            myDraw.draw_landmarks(frame, hand, mpHands.HAND_CONNECTIONS)
        
        
    #flipping the video
    frame = cv2.flip(frame, 1)

    #showing the video
    cv2.imshow('Video', frame)

    #press q to quit the video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
