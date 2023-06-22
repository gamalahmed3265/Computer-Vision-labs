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

cv.imshow("img",img)
cv.imshow("lap",lap)




k=cv.waitKey(0)
if k==27:
    cv.destroyAllWindows()