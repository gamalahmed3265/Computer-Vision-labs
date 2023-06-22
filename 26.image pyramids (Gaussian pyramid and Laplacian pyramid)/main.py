import cv2 as cv
import numpy as np
import os


def isExists(path: str):
    assert os.path.exists(path)
    

url="assets"
# imageName="early.png"
imageName="smarties.png"
# imageName="ba.png"


path=f"{url}/{imageName}"

isExists(path)
    
img=cv.imread(path)
img=cv.resize(img,(550,250)) # w,h
# img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)


lap=cv.Laplacian(img,cv.CV_64F,ksize=3)
lap=np.uint8(np.absolute(lap))

sobel_x=cv.Sobel(img,cv.CV_64F,1,0) #x,y
sobel_y=cv.Sobel(img,cv.CV_64F,0,1)#x,y

sobel_x=np.uint8(np.absolute(sobel_x))
sobel_y=np.uint8(np.absolute(sobel_y))

compine_sobel_x_y=cv.bitwise_or(sobel_x,sobel_y)

cany=cv.Canny(img,100,100) #maxVal , minVal

lr1=cv.pyrDown(img)#minmize the image
lr2=cv.pyrDown(lr1)
lr3=cv.pyrUp(lr1)#mixmize image

cv.imshow("img",img)
cv.imshow("lap",lap)
cv.imshow("lap",lap)
cv.imshow("sobel_x",sobel_x)
cv.imshow("sobel_y",sobel_y)
cv.imshow("compine_sobel_x_y",compine_sobel_x_y)
cv.imshow("cany",cany)

cv.imshow("lr1",lr1)
cv.imshow("lr2",lr2)
cv.imshow("lr3",lr3)
k=cv.waitKey(0)
if k==27:
    cv.destroyAllWindows()