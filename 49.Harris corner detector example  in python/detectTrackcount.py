import cv2
import numpy as np
from preprocessing import *
# from tracker import TrackerMaster
import mediapipe as mp
import time 

# track=TrackerMaster()

font=getFonts(2)


def DetectionTracking(frame: np.ndarray):
    himg,wimg,_=frame.shape
    
    gray=grayImage(frame)
    gray=np.float32(gray)
    dst=cv2.cornerHarris(gray,2,3,0.04)
    
    dst=cv2.dilate(dst,None)
    print(dst)
    frame[dst>0.01*dst.max()]=[0,0,255]
    
    # thr=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,85,11)
    
    cv2.imshow("frame",frame)
    cv2.imshow("thr",dst)






