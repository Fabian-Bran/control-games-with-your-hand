import cv2
import mediapipe as mp
import pyautogui
import pydirectinput


mp_drawing=mp.solutions.drawing_utils
mp_drawing_styles=mp.solutions.drawing_styles
mphands=mp.solutions.hands

#change these based on preference:
distance=70 # palm distance away from center requiered in order to begin
sensitivity=5 #higher number = slower
trigger_sensitivity=5 #how close your landmarks need to be to trigger the action

mouse_x, mouse_y = pyautogui.position() 

capture=cv2.VideoCapture(0)
hands=mphands.Hands()

#used for the mouse
def findDistanceFromCenter(x,y,target):

    x_distance = x - target[0]
    y_distance = y - target[1]
    

    return (x_distance, y_distance)

      
#used for gesture controls
def findDistanceFromTarget(x,y,target):
    x_distance = x - target.x
    y_distance = y - target.y
    x_distance = abs(x_distance * 100)
    y_distance = abs(y_distance * 100)
    return (x_distance, y_distance)

   

while True:
    #image is processed and some variables are assigned
    data,image=capture.read()
    image=cv2.cvtColor(cv2.flip(image,1),cv2.COLOR_BGR2RGB)
    img_h,img_w,_ = image.shape
    midpoint=[int(img_w/2),int(img_h/2)]
    tright=[midpoint[0] + distance,midpoint[1] + distance]
    bright=[midpoint[0] + distance,midpoint[1] - distance]
    tleft=[midpoint[0] - distance ,midpoint[1] + distance]
    bleft=[midpoint[0] - distance,midpoint[1] - distance]
    results=hands.process(image)
    image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image,hand_landmarks,mphands.HAND_CONNECTIONS)
        
        #assigning position of the wrist and the bottom of the middle finger to variables
        #the index refers to a keypoint on the hand (refer to the image included if you want to add something)
        wrist = hand_landmarks.landmark[0] 
        middle_finger_mcp = hand_landmarks.landmark[9]
        thumb_tip = hand_landmarks.landmark[4]
        index_finger_tip = hand_landmarks.landmark[8]

        
        #using the position of the wrist and the bottom of the middle finger to aproximate the palms location 
        palm_x = ((wrist.x + middle_finger_mcp.x)/2)* img_w
        palm_y = ((middle_finger_mcp.y + wrist.y) /2)* img_h

        palm_distance = findDistanceFromCenter(palm_x,palm_y,midpoint)
        thumb_index_tip_distance = findDistanceFromTarget(thumb_tip.x,thumb_tip.y,index_finger_tip)

        if thumb_index_tip_distance[0] < trigger_sensitivity and thumb_index_tip_distance[1] < trigger_sensitivity:
            pyautogui.click()
        elif palm_distance[0] > distance or palm_distance[0] < -abs(distance) or palm_distance[1] > distance or palm_distance[1] < -abs(distance):
            mouse_x += palm_distance[0] / sensitivity
            mouse_y += palm_distance[1] / sensitivity
            pydirectinput.moveTo(int(mouse_x),int(mouse_y),relative=True,_pause=False)
        else:
            pass
            

        

        
        
        
        #only shows where your palm is so you can comment this if you want.   
        cv2.circle(image,center=(int(round(palm_x)),int(round(palm_y))),radius=10,color=(255,0,0) ,thickness=6)
    

    mouse_x, mouse_y = pyautogui.position() 

    cv2.circle(image,center=(tleft),radius=10,color=(255,0,0) ,thickness=6)
    cv2.circle(image,center=(tright),radius=10,color=(255,0,0) ,thickness=6)
    cv2.circle(image,center=(bright),radius=10,color=(255,0,0) ,thickness=6)
    cv2.circle(image,center=(bleft),radius=10,color=(255,0,0) ,thickness=6)
    cv2.imshow("CS handtracker",image)
    #do not change this (from what i can tell there is no way to make it faster)
    cv2.waitKey(1)