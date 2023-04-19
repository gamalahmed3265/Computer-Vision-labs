import cv2 as cv
import numpy as np


def click_event_create_window(event,x,y,flags,param):
    if event==cv.EVENT_RBUTTONDOWN:
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        myColorsImage=np.zeros((512,512,3),dtype=np.uint8)
        myColorsImage[:]=[blue,green,red]
        cv.imshow("Color", myColorsImage)



url="C:\Projects\Collage\ML\computer vision\image"
img=f"{url}\gamal.jpg"
img=cv.imread(img)

img=cv.resize(img,(512,512))
cv.imshow("image",img)

cv.setMouseCallback("image",click_event_create_window)

k=cv.waitKey(0)

if k==27:
    cv.destroyAllWindows()


