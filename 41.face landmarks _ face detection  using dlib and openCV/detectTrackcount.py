import cv2
import numpy as np
from preprocessing import grayImage,resize
from tracker import TrackerMaster

import dlib

print(dlib.__version__)

track=TrackerMaster()
# font=cv2.FONT_HERSHEY_PLAIN
# font=cv2.FONT_HERSHEY_SIMPLEX
font=cv2.FONT_HERSHEY_COMPLEX


detector=dlib.get_frontal_face_detecor()
predictor=dlib.shape_predictor("shape_predicor_68_face_landmarks.dat")



def DetectionTracking(frame: np.ndarray):
    gray=grayImage(frame)
    faces=detector(gray)
    for face in faces:
        x1=face.left()
        y1=face.top()
        x2=face.righs()
        y2=face.bottom()
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),3)
        landmarks=predictor(gray,face)
        for n in range(0,68):
            x=landmarks.part(n).x
            y=landmarks.part(n).y
            cv2.circle(frame,(x,y),3,(0,255,0),-1)
            
    cv2.imshow("frame",frame)    
        





