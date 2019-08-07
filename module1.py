import cv2

img = cv2.imread(r'D:\opencv\sources\samples\data\lena.jpg')
cv2.imshow('hello world',img)
cv2.waitKey()
cv2.destroyAllWindows()
