import cv2 as cv
import numpy as np


url="C:\Projects\Collage\ML\computer vision\image"
img=f"{url}\gamal.jpg"

def getEvent():
    events=[i for i in dir(cv) if "EVENT" in i]
    print(events)

def findPostions(event,x,y,flag,param):
    if event==cv.EVENT_LBUTTONDOWN:
        print(x,y)

img=cv.imread(img)

# print(img.shape) # (720, 1280, 3)
# print(img.size)  # 2764800
# print(img.dtype) # uint8

b,g,r=cv.split(img) #split img to 3 channel blue,green , red
# print(b,g,r)

img=cv.merge((b,g,r)) # merge 3 channel to img
# print(img)

img=cv.resize(img,(512,512))

partOfImage=img[300:400,330:500] #y2:y1, x2:x1

# dst=cv.addWeighted(img,.5,img2,.5,100)

img[100:200,130:300]=partOfImage

cv.imshow("image",img)
cv.imshow("partOfImage",partOfImage)

#getEvent()
#cv.setMouseCallback("image",findPostions)


k=cv.waitKey(0)

if k==27:
    cv.destroyAllWindows()


