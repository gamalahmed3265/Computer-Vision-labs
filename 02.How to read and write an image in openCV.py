import cv2 as cv


img="../image/test.png"
img=cv.imread(img,0)

print(img)

cv.imshow("img",img)

k=cv.waitKey(0)
if k==27:
    cv.destroyAllWindows()
elif ord("s"):
    cv.imwrite("this a new",img)
    cv.destroyAllWindows()