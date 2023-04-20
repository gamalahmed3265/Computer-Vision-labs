import cv2 as cv
import numpy as np


   
def noThing(x):
    print(x)




url="C:\Projects\Collage\ML\computer vision\image"
img=f"{url}\shape.png"

frame=cv.imread(img)
frame=cv.resize(frame,(400,400))


# create windows name image
cv.namedWindow("Traching")

# set track : name of track and name of window
cv.createTrackbar("LH","Traching",0,255,noThing)
cv.createTrackbar("LS","Traching",0,255,noThing)
cv.createTrackbar("LV","Traching",0,255,noThing)
cv.createTrackbar("UH","Traching",255,255,noThing)
cv.createTrackbar("US","Traching",255,255,noThing)
cv.createTrackbar("UV","Traching",255,255,noThing)


while(1):
    
    cv.imshow("Traching",frame)
    
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)    
   
    # get track value by the name of track and name of window
    lh=cv.getTrackbarPos("LH","Traching")
    ls=cv.getTrackbarPos("LS","Traching")
    lh=cv.getTrackbarPos("LH","Traching")
    
    uh=cv.getTrackbarPos("UH","Traching")
    us=cv.getTrackbarPos("US","Traching")
    uv=cv.getTrackbarPos("UV","Traching")
    
    
    l_p=np.array([lh,ls,lh])
    u_p=np.array([uh,us,uv])
    
    mask=cv.inRange(hsv,l_p,u_p)
    
    res=cv.bitwise_and(frame,frame,mask=mask) #Threshold the HSV IMAGE
    
 
    cv.imshow("frame",frame)
    cv.imshow("hsv",hsv)
    cv.imshow("mask",mask)
    cv.imshow("res",res)
    
     
    
    k=cv.waitKey(1)
    # key from key borads 
    if k ==27:
        break
    
# remove screen image
    
cv.destroyAllWindows()



