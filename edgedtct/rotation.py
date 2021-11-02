import cv2
import numpy as np

canvas = np.zeros((840, 840, 3))
canvas[:] = [255, 255, 255]

# scaling
img = cv2.imread('linkedinDP.jpg')

lin_res = cv2.resize(img, None, fx=5.5, fy=5.5, interpolation=cv2.INTER_CUBIC)

cv2.imshow("mm", lin_res)
cv2.waitKey(0)