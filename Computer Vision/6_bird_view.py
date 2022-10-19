import cv2
import numpy as np

img = cv2.imread('cards.jpeg')

width,height = 250,350
pts1 =np.float32([[131,42],[231,79],[22,116],[143,201]])
print(pts1)
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
img_out = cv2.warpPerspective(img,matrix,(width,height))

for x in range(0,4):
    cv2.circle(img,(int(pts1[x][0]),int(pts1[x][1])),4,(0,0,255),cv2.FILLED)

cv2.imshow('Image_Output', img_out)
cv2.imshow('Image',img)
cv2.waitKey(0)