
import cv2 as cv

filename = r'E:\opencv\sources\samples\data\lena.jpg'
img = cv.imread(filename)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow("source image",img)
cv.imshow("gray",gray)
cv.waitKey(1)
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

cv.imshow("hue",hsv[:,:,0])           #0,1,2代表三个不同的通道
cv.imshow("saturation",hsv[:,:,1])   #img(:,:,0)代表第零个通道x，y方向的所有行所有列。
cv.imshow("value",hsv[:,:,2])
cv.waitKey(1)

cv.imshow("Blue",img[:,:,0])
cv.imshow("Green",img[:,:,1])
cv.imshow("Red",img[:,:,2])
cv.waitKey()
cv.destroyAllWindows()
