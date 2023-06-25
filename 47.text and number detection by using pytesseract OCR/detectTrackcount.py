import cv2
import numpy as np
from preprocessing import *
from tracker import TrackerMaster
import mediapipe as mp
import time 
import pytesseract

track=TrackerMaster()

font=getFonts(2)
pytesseract.pytesseract.tesseract_cmd="dir"


def DetectionTracking(frame: np.ndarray):
    himg,wimg,_=frame.shape
    
    gray=grayImage(frame)
    thr=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,85,11)
    config="--psm 3" #page segmentation
    pytesseract.pytesseract.tesseract_cmd
    # text=pytesseract.image_to_string(img ,config ,lan="eng)
    # print(text)
    boxes=pytesseract.image_to_boxes(img,lang="eng")
    for b in boxes.splitlines():
        print(b)
        b.split(" ")
        text,x,y,w,h=b
        cv2.rectangle(frame,(x,himg-y),(x+w,himg+h),(250,225,85),3)
        cv2.putText(img,text,(x,himg-y),font,1,(255,0,0),3)
    cv2.imshow("frame",frame)
    cv2.imshow("frame",thr)






