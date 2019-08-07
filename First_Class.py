
import cv2 as cv

filename = '/home/m/Documents/data/lena.jpg'
img = cv.imread(filename)
Gauss = cv.GaussianBlur(img,(5,5),2000)#高斯滤波
Media = cv.medianBlur(img,5) #中值滤数学形态学滤波

cv.imshow("Gaussian",Gauss)
cv.imshow("media",Media)
cv.waitKey()