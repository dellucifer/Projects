# Importing OpenCV
import cv2

# Importing Image and configuring it
img = cv2.imread('cards.jpeg')
print(img.shape)

width,height = 400,400
img_resize = cv2.resize(img,(width,height))
print(img_resize.shape)
img_crop = img[30:300,300:500]

# Showing Image
cv2.imshow('Imgae', img)
# cv2.imshow('Resized_Image',img_resize)
cv2.imshow('Cropped_Image',img_crop)
cv2.waitKey(0)
