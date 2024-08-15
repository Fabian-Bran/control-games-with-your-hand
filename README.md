# control-games-with-your-hand
 Uses mediapipe modual to interact with video games.

 This was tuned for Counter-Strike however, it is quite easy to change the sensitivity and the distance required to move your palm away from the center. Adjusting the gesture controls may be slightly trickier, so I will leave the indexes for the different landmarks along with a image to use as a reference.

 WRIST_IDX = 0
 THUMB_CNC_IDX=1
 THUMB_MCP_IDX=2
 THUMB_IP_IDX=3
 THUMB_TIP_IDX=4
 INDEX_FINGER_MCP_IDX=5
 INDEX_FINGER_PIP_IDX=6
 INDEX_FINGER_DIP_IDX=7
 INDEX_FINGER_TIP_IDX=8
 MIDDLE_FINGER_MCP_IDX=9
 MIDDLE_FINGER_PIP_IDX=10
 MIDDLE_FINGER_DIP_IDX=11
 MIDDLE_FINGER_TIP_IDX=12
 RING_FINGER_MCP_IDX=13
 RING_FINGER_PIP_IDX=14
 RING_FINGER_DIP_IDX=15
 RING_FINGER_TIP_IDX=16
 PINKY_MCP_IDX=17
 PINKY_PIP_IDX=18
 PINKY_DIP_IDX=19
 PINKY_TIP_IDX=20

 For a better understanding look at:
 https://ai.google.dev/edge/mediapipe/solutions/guide?_gl=1*9b7tv9*_up*MQ..*_ga*MzEyNzgyNjc0LjE3MjM2ODAzMjk.*_ga_P1DBVKWT6V*MTcyMzY4MDMyOS4xLjAuMTcyMzY4MDMzNi4wLjAuNDkwOTU5MzMy

 Check out this repository, as it was what inspired this one:
 https://github.com/Jakelrnr/Handtracking/blob/main/Basic%20hand%20and%20joint%20tracking
