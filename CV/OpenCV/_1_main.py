import cv2
import numpy as np

"""
Image theory:
1. Image is a 2D array of pixels.
2. Each pixel has a color value, which is represented as a tuple of three values (B, G, R) for color images and a single value for gray scale images.
3. The color values are in the range of 0 to 255, where 0 represents black and 255 represents white for gray scale images, and for color images, (0, 0, 0) represents black and (255, 255, 255) represents white.   
"""

#Read an Image
img = cv2.imread("./img/fruits.png")
print(type(img))
print(img)

#Show the Image
cv2.imshow("window", img) 
cv2.waitKey(0) 
#"window" the name of the window that will be created to display the image
# 0 in waitkey means wait indefinitely.

#Show in particular ratio
img = cv2.resize(img, (600, 600)) # (width, height)
cv2.imshow("window", img)
cv2.waitKey(0)

#Gray Scale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("window", img_gray)
cv2.waitKey(0)
print(img_gray.shape) 
#shape gives the dimension of image.
#since gray scale image has only one channel, the shape is (600, 600) instead of (600, 600, 3) for color image.
#The shape of the image is represented as (height, width, channels) for color images and (height, width) for gray scale images.
#As size of img is defined as (600, 600) hence shape gives out the dimensions of the image as (600, 600) for gray scale image.

#RGB Color channels
img[:, :, 0] = 0 # Blue channel
img[:, :, 1] = 0 # Green channel    
cv2.imshow("window", img)
cv2.waitKey(0)
# B G R channels are represented as 0, 1, and 2 respectively in the image array.
# [: , : , 0] means all rows, all columns, and the first channel (Blue) of the image.
# [: , : , 1] means all rows, all columns, and the second channel (Green) of the image.
# [: , : , 2] means all rows, all columns, and the third channel (Red) of the image.
# [: , : , channel] = 0 sets the specified channel to 0, effectively removing that color from the image. In this case, setting the Blue and Green channels to 0 leaves only the Red channel, resulting in an image that appears red.