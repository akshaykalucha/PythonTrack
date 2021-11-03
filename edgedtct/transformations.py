import cv2
import numpy as np
from numpy.lib.function_base import disp

# euclidean and isometic
# affine
# projective transforms

# 1) GEOMETRIC TRANSFORMATION
# Transformation is modifying spatial relationship between pixels
# 2) image can be shifted,rotated ans streched in multiple ways

# --> Euclidean and Isometric transform:
# Whenever an image is shifted(translation) in x or y axis or rotated is euclidean or isometric transform
# Euclidean transform is a subset of affine transform
#      -- R is an orthogonal matrix
#      -- Euclidean distance is preserved
#      -- Has three degrees of freedom, two for translation and one for rotation
#      -- Characterstics include: Distance, Angles and Shaped remains preserved


# load the image 
img = cv2.imread('linkedinDP.jpg')

# Translation matrix
matrix = np.float32([[1,0,100], [0,1,100]])

# apply matrix to the image, affine  is generalisation of euclidean transformation
translated = cv2.warpAffine(img, matrix, (img.shape[1]+100, img.shape[0]+100))


# Affine transformation

# --> Affine transformation has six degrees of freedom, two for translation, one for rotation, one for scaling
#     one for scaling direction and one for scaling ratio
# In short in affine transformation the matrix can rotated, translated, scaled and sheared

# In Affine transformation parallel line will be preserved but maybe sheared or streched, ex: squares may become
# parallelogram

# using a 2x3 matrix and warpAffine function i can rotate, shear, translate or scale matrix

rows, cols = img.shape[:2]

src_points = np.float32([[0,0], [cols-1, 0], [0, rows-1]])
dist_points = np.float32([[0,0], [int(0.6*(cols-1)), 0], [int(0.4*(cols-1)), rows-1]])

affine_matrix = cv2.getAffineTransform(src_points, dist_points)
output = cv2.warpAffine(img, affine_matrix, (cols, rows))