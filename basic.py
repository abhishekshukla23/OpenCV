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
cany=cv.Canny(img,125,175)
cv.imshow('Canny Edges',cany)
cany=cv.Canny(blur,125,175)
cv.imshow('Canny Edges',cany)

# dilating the image

dilated=cv.dilate(cany,(7,7),iterations=1)

cv.imshow('dilated',dilated)

#Eroding 

eroded=cv.erode(dilated,(3,3),iterations=1)

cv.imshow('eroded',eroded)


# Resize 

resized=cv.resize(img,(500,500))

cv.imshow('Resized',resized)

#cropping


cropped=img[50:400, 300:400]

cv.imshow('cropped',cropped)


 





cv.waitKey(0)