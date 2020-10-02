
''' Steps:
    1. Capture and store the background frame.
    2. Detect the red colored cloth using color detection and segmentation algorithm.
    3. Segment out the red colored cloth by generating a mask.
    4. Generate the final augmented output to create a magical effect. '''


import cv2
import time
import numpy as np

cam = cv2.VideoCapture(0)

# capturing the background in range of 60 
for i in range(60):
    ret,background = cam.read()

background = cv2.flip(background,1)

while True:
    ret,frame = cam.read()
    frame = cv2.flip(frame,1)
    
    # converting BGR to HSV for better
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # ranges should be carefully chosen 
    # setting the lower and upper range for mask1
    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])
    mask1 = cv2.inRange(hsv,lower_red,upper_red)
 
    # setting the lower and upper range for mask2
    lower_red = np.array([170,120,70])
    upper_red = np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower_red,upper_red)

     ''' the above block of code could be replaced with 
         some other code depending upon the color of your cloth '''

    mask1 = mask1+mask2

    # Refining the mask corresponding to the detected red color
    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=2)
    mask1 = cv2.dilate(mask1,np.ones((3,3),np.uint8),iterations=1)
    mask2 = cv2.bitwise_not(mask1)

    # Generating the final output
    res1 = cv2.bitwise_and(background,background,mask=mask1)
    res2 = cv2.bitwise_and(frame,frame,mask=mask2)
    final_output = cv2.addWeighted(res1,1,res2,1,0)

    cv2.imshow('Invisibility Cloak',final_output)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
