import cv2 as cv
import numpy as np


def click_event_draw(event,x,y,flags,param):
    global img,points
    if event ==cv.EVENT_LBUTTONDOWN:
        cv.circle(img,(x,y),3,(143,32,23),-1)
        points.append((x,y))
        # print(len(points))
        if len(points)>=2:
            # print(points[-1],points[-2])
            cv.line(img,points[-1],points[-2],(0,220,220),3)
        # if  len(points)>10:
        #     font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        #     img=cv2.putText(img,"finsh",(x,y),font,.5,(200,250,0),2)
        cv.imshow("image",img)


img=np.zeros((400,400,3))
points=[]

cv.imshow("image",img)

cv.setMouseCallback("image",click_event_draw)

k=cv.waitKey(0)

if k==27:
    cv.destroyAllWindows()


