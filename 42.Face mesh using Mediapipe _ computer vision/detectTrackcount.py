import cv2
import numpy as np
from preprocessing import grayImage,resize
from tracker import TrackerMaster
import mediapipe as mp

track=TrackerMaster()
# font=cv2.FONT_HERSHEY_PLAIN
# font=cv2.FONT_HERSHEY_SIMPLEX
font=cv2.FONT_HERSHEY_COMPLEX

def DetectionTracking(frame: np.ndarray):
    # gray=grayImage(frame)

    mp_face_mesh=mp.solutions.face_mesh.FaceMesh()
    
    rgb_img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=mp_face_mesh.process(rgb_img)
    # print(len(results.multi_face_landmarks))
    w,h,_=frame.shape
    for focial_landmarks in results.multi_face_landmarks:
        for i in range(0,468):
            pt1=focial_landmarks.landmark[i]
            # print(pt1)
            
            x=int(pt1.x * w)
            y=int(pt1.y * h)
            # print(x,y)
            
            cv2.circle(frame,(x,y),2,(233,213,42),-1)
            
    cv2.imshow("frame",frame)    
        





