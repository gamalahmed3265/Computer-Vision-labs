import cv2
import numpy as np
from preprocessing import *
from tracker import TrackerMaster
import mediapipe as mp
import time 
import pytesseract

track=TrackerMaster()

font=getFonts()
pytesseract.pytesseract.tesseract_cmd="dir"


def DetectionTracking(frame: np.ndarray):
    gray=grayImage(frame)
    thr=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,85,11)
    config="--psm 3" #page segmentation
    pytesseract.pytesseract.tesseract_cmd
    text=pytesseract.image_to_string(img ,config ,lan="eng)
    print(text)
    
    cv2.imshow("frame",frame)
    cv2.imshow("frame",thr)






