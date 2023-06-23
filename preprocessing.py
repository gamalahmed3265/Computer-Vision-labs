import cv2 as cv
import numpy as np
import os


def isExists(path: str):
    assert os.path.exists(path)
    
def resize(img :np.ndarray,scale_percent=30,flag:bool=True):
    
    if flag:
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        #dsize
        dsize = (width, height)
        img = cv.resize(img, dsize)
    else:
        img=cv.resize(img,(512,512)) # w,h
    return img
    