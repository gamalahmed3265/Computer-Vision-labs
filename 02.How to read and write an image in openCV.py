import cv2 as cv


img="../image/test.png"
img=cv.imread(img,0)
#   0 for grayscale
#   1 for color
#  -1 for channel


cv.imshow("img",img)

k=cv.waitKey(0)# 5000 ms(millsec) 5 sec 
if k==27:
    cv.destroyAllWindows()
elif ord("s"):
    cv.imwrite("this a new",img)
    cv.destroyAllWindows()