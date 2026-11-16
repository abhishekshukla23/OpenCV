import cv2 as cv
import numpy as np


blank=np.zeros((500,500,3),dtype='uint8')

cv.imshow('blank',blank)

# img=cv.imread('photos/spidermanTwo.jpg')

# cv.imshow('Spiderman',img)


## Paint the image with certain color

# blank[:]=0,255,0

# blank[200:300,300:400]=0,255,0

# Draw a reactangle

# cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,0),thickness=-1)
#cv.imshow('rectangle',rectangle)
## Draw a circle

# cv.circle(blank,(250,250),250,(0,0,255),thickness=-1)

# cv.imshow('circle',blank)


##Draw a line

# cv.line(blank,(100,290),(blank.shape[1]//2,blank.shape[0]//2),(255,255,0))

# cv.imshow('line',blank)


#.Write text on image

cv.putText(blank,'Hello I am Abhishek !!',(0,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),thickness=2)
cv.imshow('text',blank)

cv.waitKey(0)