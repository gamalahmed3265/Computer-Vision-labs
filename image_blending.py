import cv2
import numpy as np

def ImageBlending(img1,img2):
    
    #mearge two image
    
    #cut the image
    img1_img2=np.hstack((img1[:,235:523],img2[:,200:488]))
    
    # print(img1_img2)
    #genrate gaussian pyramids for img1
    img1_copy=img1.copy()
    ga_img1=[img1_copy]
    for i in range(6):
        img1_copy=cv2.pyrDown(img1_copy)
        ga_img1.append(img1_copy)
     
    #genrate laplacian pyramids for img1
    img1_copy=ga_img1[5]
    lap_img1=[img1_copy]
    for i in range(5,0,-1):
        gaussian_expanded=cv2.pyrUp(ga_img1[i])
        lapacian=cv2.subtract(ga_img1[i],gaussian_expanded)
        lap_img1.append(lapacian)
         

    #genrate gaussian pyramids for img2
    img2_copy=img2.copy()
    ga_img2=[img2_copy]
    for i in range(6):
        img2_copy=cv2.pyrDown(img2_copy)
        ga_img2.append(img2_copy)
        
    #genrate laplacian pyramids for img2
    img2_copy=ga_img2[5]
    lap_img2=[img2_copy]
    for i in range(5,0,-1):
        gaussian_expanded=cv2.pyrUp(ga_img2[i])
        lapacian=cv2.subtract(ga_img2[i-1],gaussian_expanded)
        lap_img2.append(lapacian)
     
    #now add left image and right image
    imag1_imag2_pyramids=[]
    
    for lap1,lap2 in zip(lap_img1,lap_img2):
        cols,row,sh=lap1.shape
        lapacian=np.hstack((lap1[:,0:int(cols/2)],lap2[:,int(cols/2):]))
        imag1_imag2_pyramids.append(lapacian)
    
    #now reconstruct
    img1_img2_reconstruct=imag1_imag2_pyramids[0]
    cv2.imshow("img 0",img1_img2_reconstruct)
    for i in range(1,6):
        img1_img2_reconstruct=cv2.pyrUp(img1_img2_reconstruct)
        img1_img2_reconstruct=cv2.add(imag1_imag2_pyramids[i],img1_img2_reconstruct)
    
    #show image
    cv2.imshow("img 1",img1)
    cv2.imshow("img 2",img2)
    cv2.imshow("img1_img2_reconstruct",img1_img2_reconstruct)
    # cv2.imshow("img1_img2",img1_img2)
    

