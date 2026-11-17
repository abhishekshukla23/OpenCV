import cv2 as cv
import numpy as np

##masking-->allows to focus on certain part of images and removes unwanted parts


img=cv.imread('photos/spidermanTwo.jpg')
cv.imshow('Spiderman',img)


blank=np.zeros(img.shape[:2],dtype='uint8')

cv.imshow('Blank Image',blank)

mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2-100),100,255,-1)

cv.imshow('Mask',mask)

masked=cv.bitwise_and(img,img,mask=mask)

cv.imshow("masked image",masked)


cv.waitKey(5000)