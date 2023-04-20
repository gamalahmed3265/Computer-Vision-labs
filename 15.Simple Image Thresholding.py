import cv2 as cv
import numpy as np


   
def noThing(x):
    print(x)




url="C:\Projects\Collage\ML\computer vision\image"
img=f"{url}\shape.png"


img=cv.imread(img,0)
img=cv.resize(img,(400,400))

_,thr1=cv.threshold(img,55,255,cv.THRESH_BINARY)
_,thr2=cv.threshold(img,200,255,cv.THRESH_BINARY_INV)
_,thr3=cv.threshold(img,127,255,cv.THRESH_TRUNC)
_,thr4=cv.threshold(img,127,255,cv.THRESH_TOZERO)
_,thr5=cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

cv.imshow("thr1",thr1)
cv.imshow("thr2",thr2)
cv.imshow("thr3",thr3)
cv.imshow("thr4",thr4)
cv.imshow("thr5",thr5)

k=cv.waitKey(0)
if k==27:
    cv.destroyAllWindows()

# plt.imshow(img)


