import cv2 as cv
import numpy as np



url="C:\Projects\Collage\ML\computer vision\image"
img=f"{url}\shape.png"

frame=cv.imread(img)
frame=cv.resize(frame,(400,400))
while 1:
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    l_p=np.array([110,50,50])
    u_p=np.array([130,255,255])
    
    mask=cv.inRange(hsv,l_p,u_p)
    
    res=cv.bitwise_and(frame,frame,mask=mask) #Threshold the HSV IMAGE

    cv.imshow("frame",frame)
    cv.imshow("hsv",hsv)
    cv.imshow("mask",mask)
    cv.imshow("res",res)
    
    k=cv.waitKey(0)
    # key from key borads 
    if k ==27:
        break
        
cv.destroyAllWindows()


