import cv2 as cv

img=cv.imread('photos/spidermanTwo.jpg')
cv.imshow('Spiderman',img)

# Averaging

average=cv.blur(img,(8,8))
cv.imshow('Average Blur',average)

# Gaussian Blur

gauss=cv.GaussianBlur(img,(7,7),0)
cv.imshow('gauss blur',gauss)

#Median Blur

median=cv.medianBlur(img,7)
cv.imshow('median blur',median)

#Bilateral Blur

bilat=cv.bilateralFilter(img,5,45,55)
cv.imshow('bilateral',bilat)

cv.waitKey(5000)