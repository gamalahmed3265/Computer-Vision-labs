import cv2 as cv
import numpy as np


url="C:\Projects\Collage\ML\computer vision\image"
img=f"{url}\gamal.jpg"

# and *
# or +
# not !
# xor 0,0=0 1,1=0    1,0=1 ,0,1=1

img1=np.zeros((250,500,3),dtype=np.uint8)
cv.rectangle(img1,(200,0),(300,200),(255,255,255),-1)

img2=np.full((250,500,3),255,dtype=np.uint8)
cv.rectangle(img2,(0,0),(250,250),(0,0,0),-1)

bit_add=cv.bitwise_and(img1,img2)
bit_or=cv.bitwise_or(img1,img2)
bit_xor=cv.bitwise_xor(img1,img2)
bit_not=cv.bitwise_not(img1,img2)

cv.imshow("imge",img1)
cv.imshow("imge2",img2)

cv.imshow("bit_add",bit_add)
cv.imshow("bit_or",bit_or)
cv.imshow("bit_xor",bit_xor)
cv.imshow("bit_not",bit_not)

k=cv.waitKey(0)
if k==27:
    cv.destroyAllWindows()


