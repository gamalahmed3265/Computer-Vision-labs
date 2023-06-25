import cv2
import numpy as np
from preprocessing import *
from tracker import TrackerMaster
import mediapipe as mp
import time 

cascade_src="case1.xml"
track=TrackerMaster()

font=getFonts()

# line1=((160,60),(235,67))
# line2=((80,110),(218,129))

# line a
ax1=70
ay=90
ax2=230

# line b
bx1=15
by=125
bx2=225
def getSpeed(time):
    try:
        return (9.144/1000)/(time/3600)
    except:
        print('can not divid by zero')
        return 0

counterCar=1
start_time=time.time()

car_cascade=cv2.CascadeClassifier(cascade_src)

def DetectionTracking(frame: np.ndarray):
    # bluring to have exacter detections
    blur=cv2.blur(frame ,ksize=(15,15))
    
    gray=grayImage(blur)
    cars=car_cascade.detectMultiScale
    
    cv.line(frame,(ax1,ay),(ax2,ay),(255,0,0),2)
    cv.line(frame,(bx1,by),(bx2,by),(255,0,0),2)

    for (x,y,w,h) in cars:
        cv2.line(frame,(x,y),(x+w,y+h),(244,21,56),2)
        cv2.circle(frame,((int(x+x+w)/2),(int(y+y+h)/2)),(244,21,56),-1)
        
        while int (ay) ==int((y+y+h)/2):
            start_time=time.time()
            break
        while int (ay) <=int((y+y+h)/2):
            cv2.line(frame,(bx1,by),(bx2,by),(0,255,56),2)
            speed=getSpeed(time.time() - start_time)
            
            print(f"num.{counterCar} speed: {speed}")
            global counterCar
            counterCar+=1
            break
    # bfilter=cv2.bilateralFilter(gray,11,17,17) #noise reduction
    # edage=cv2.Canny(bfilter,30,300)
    # contours=cv2.findContours(edage,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # print(keypoints)
    
    
    
    cv2.imshow("frame",frame)
    # cv2.imshow("threshold",threshold)
    # cv2.imshow("gray",gray)
    # cv2.imshow("bfilter",edage)
    





