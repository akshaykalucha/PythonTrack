import cv2
import numpy as np

canvas = np.zeros((840, 840, 3))
canvas[:] = [255, 255, 255]

# scaling
img = cv2.imread('linkedinDP.jpg')

lin_res = cv2.resize(img, None, fx=5.5, fy=5.5, interpolation=cv2.INTER_CUBIC)

# translation
# translation matrix(M)

matrix = np.float32([[1,0,50], [0,1,100]])
# apply M to the image
translated = cv2.warpAffine(img, matrix, (img.shape[1]+100, img.shape[0]+100))