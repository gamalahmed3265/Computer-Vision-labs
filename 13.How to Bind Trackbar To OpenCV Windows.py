import cv2 as cv
import numpy as np



def noThing(x):
    print(x)
    # pass

img=np.zeros((300,512,3),dtype=np.uint8)
# create windows name image
cv.namedWindow("image")

# set track : name of track and name of window
cv.createTrackbar("B","image",0,255,noThing)
cv.createTrackbar("G","image",0,255,noThing)
cv.createTrackbar("R","image",0,255,noThing)

switch="O OFF\n1: ON"
cv.createTrackbar(switch,"image",0,1,noThing)

while(1):
    # show image im new windows its'name image
    cv.imshow("image",img)
    k=cv.waitKey(1)
    # key from key borads 
    if k ==27:
        break
    # get track value by the name of track and name of window
    b=cv.getTrackbarPos("B","image")
    g=cv.getTrackbarPos("G","image")
    r=cv.getTrackbarPos("R","image")
    s=cv.getTrackbarPos(switch,"image")
    # if its no its no work , or on its work 
    if s==0:
        img[:]=0 # make the color is black
    else:
        img[:]=[b,g,r] # indifer the volor by valus b , g ,r
# remove screen image
cv.destroyAllWindows()
