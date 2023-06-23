import cv2
import numpy as np
from preprocessing import grayImage,resize
from tracker import TrackerMaster

track=TrackerMaster()
font=cv2.FONT_HERSHEY_PLAIN
BGS= cv2.createBackgroundSubtractorMOG2(history=100)

 
# 451 160
# 342 290
 

# 750,450

def DetectionTracking(frame: np.ndarray,count:int):
    
    roi=frame[100:300,300:500]
    
    #subtrationg
    mask=BGS.apply(roi)
    
    _,mask=cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
    
    contours,hierarchy=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        
    detetions=[]    
    for cnt in contours:
        area=cv2.contourArea(cnt)
        
        if area>100:
            x,y,w,h=cv2.boundingRect(cnt)
            
            detetions.append([x,y,w,h])
        
    box_ids=track.update(detetions)
    for box_id in box_ids:
        x,y,w,h,idd=box_id
            
        cv2.putText(roi,str(idd),(x,y),font,1,(244,45,2),4)
        cv2.rectangle(roi,(x,y),(x+w,y+h),(0,255,0),3)
    
    cv2.imshow("frame",frame)
    cv2.imshow("roi",roi)
    cv2.imshow("mask",mask)






