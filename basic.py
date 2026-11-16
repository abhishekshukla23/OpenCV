import cv2 as cv


img=cv.imread('photos/spidermanTwo.jpg')

cv.imshow('spiderman',img)


## Converting to grayscale

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow('Gray',gray)

# Blur

blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)

cv.imshow('Blur',blur)

# Edge Cascade

cany=







cv.waitKey(0)