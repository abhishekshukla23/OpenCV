import cv2 as cv
import numpy as np
img=cv.imread('photos/spidermanTwo.jpg')

cv.imshow('spiderman',img)

#Simple thresholding

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow('Gray',gray)

threshold,thresh=cv.threshold(gray,100,255,cv.THRESH_BINARY)

cv.imshow('Simple Thresholded',thresh)



threshold,thresh_inv=cv.threshold(gray,100,255,cv.THRESH_BINARY_INV)

cv.imshow('Simple Thresholded',thresh_inv)



## Adaptive thresholding
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11,1)
cv.imshow('adaptive thresholding',adaptive_thresh)



cv.waitKey(5000)