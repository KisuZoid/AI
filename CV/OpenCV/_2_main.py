from hmac import new

import cv2
import numpy as np

image = cv2.imread("./img/fruits.png")

imgBlue = image[:, :, 0]
imgGreen = image[:, :, 1]
imgRed = image[:, :, 2]

new_img = np.hstack((imgBlue, imgGreen, imgRed))
# np.hstack() is a function in the NumPy library that horizontally stacks arrays.
img_resized = cv2.resize(new_img, (600, 600)) # (width, height)
cv2.imshow("window", img_resized)
cv2.waitKey(0)